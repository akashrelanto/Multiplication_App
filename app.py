from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Template as a Python string
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table Generator Till 1000</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            padding: 40px;
            max-width: 600px;
            width: 100%;
        }
        
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .form-group {
            text-align: center;
            margin-bottom: 30px;
        }
        
        label {
            display: block;
            margin-bottom: 10px;
            font-size: 1.2em;
            color: #555;
            font-weight: 600;
        }
        
        input[type="number"] {
            padding: 15px 20px;
            font-size: 18px;
            border: 2px solid #e1e5e9;
            border-radius: 10px;
            width: 200px;
            text-align: center;
            transition: all 0.3s ease;
            margin-right: 15px;
        }
        
        input[type="number"]:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        input[type="submit"] {
            padding: 15px 30px;
            font-size: 16px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
        }
        
        input[type="submit"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }
        
        .table-container {
            margin-top: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 15px;
            border-left: 5px solid #667eea;
        }
        
        .table-container h2 {
            color: #333;
            margin-bottom: 20px;
            text-align: center;
            font-size: 1.8em;
        }
        
        .multiplication-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 10px;
            margin-top: 20px;
        }
        
        .multiplication-item {
            background: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 1.1em;
            color: #333;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease;
        }
        
        .multiplication-item:hover {
            transform: scale(1.05);
        }
        
        .error-message {
            background: #ffe6e6;
            color: #d63031;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            border-left: 5px solid #d63031;
        }
        
        .success-message {
            background: #e6ffe6;
            color: #00b894;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            border-left: 5px solid #00b894;
        }
        
        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }
            
            h1 {
                font-size: 2em;
            }
            
            input[type="number"] {
                width: 100%;
                margin-right: 0;
                margin-bottom: 15px;
            }
            
            .multiplication-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔢 Multiplication Table Generator</h1>
        
        <div class="form-group">
            <form method="POST">
                <label for="number">Enter a number to generate its multiplication table:</label>
                <br><br>
                <input type="number" name="number" id="number" placeholder="Enter number..." required min="1" max="1000">
                <input type="submit" value="Generate Table">
            </form>
        </div>
        
        {% if error %}
            <div class="error-message">
                <strong>Error:</strong> {{ error }}
            </div>
        {% endif %}
        
        {% if table and number %}
            <div class="table-container">
                <h2>📊 Multiplication Table for {{ number }}</h2>
                <div class="multiplication-grid">
                    {% for line in table %}
                        <div class="multiplication-item">
                            {{ line }}
                        </div>
                    {% endfor %}
                </div>
            </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def multiplication_table():
    table = []
    number = None
    error = None
    
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            
            # Validate input
            if number < 1:
                error = "Please enter a positive number greater than 0."
            elif number > 1000:
                error = "Please enter a number less than or equal to 1000."
            else:
                # Generate multiplication table from 1 to 20 for better learning
                table = [f"{number} × {i} = {number * i}" for i in range(1, 21)]
                
        except ValueError:
            error = "Invalid input. Please enter a valid number."
        except Exception as e:
            error = f"An error occurred: {str(e)}"
    
    return render_template_string(HTML_TEMPLATE, table=table, number=number, error=error)

if __name__ == '__main__':
    # This host is allowed so that it can be accessed from outside the docker as well.
    app.run(host="0.0.0.0", debug=True, port=5000)
