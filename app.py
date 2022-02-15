from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

def change(amount):
    # calculate the resultant change and store the result (res)
    res = []
    coins = [1,5,10,25] # value of pennies, nickels, dimes, quarters
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

    # divide the amount*100 (the amount in cents) by a coin value
    # record the number of coins that evenly divide and the remainder
    coin = coins.pop()
    num, rem  = divmod(int(amount*100), coin)
    # append the coin type and number of coins that had no remainder
    res.append({num:coin_lookup[coin]})

    # while there is still some remainder, continue adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num:coin_lookup[coin]})
    return res


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("Johnny WAS HERE")
    return 'Johnny WAS HERE'

@app.route('/change/<dollar>/<cents>')
def changeroute(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    result = change(float(amount))
    return jsonify(result)

@app.route('/multiply/<dollar>/<cents>')
def multiply(dollar, cents):
    AMOUNT = f"{dollar}.{cents}"
    scen1_mult = float(AMOUNT) * int(100)
    scen2_mult = float(AMOUNT) * int(1000)
    Scenario_1 = f"Dollars: ${dollar}, cents: {cents}, This is the CHANGE X 100: {float(scen1_mult) }  <br> "
    Scenario_2 = f"Dollars: ${dollar}, cents: {cents}, This is the CHANGE X 1000: {float(scen2_mult) } <br> "

    return Scenario_1 + Scenario_2

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method =="GET":
        return f'''<h1>Login</h1>
                <form action="#" method="post">
                <ol>
                    <li> Add a Dollar Amount: </p>
                    <p> <input type="text" name="dollar_amt"  value=""/></p>
                    <li> Add number of cents; (must be less than 100) </li>

                    <p> <input type="text" name="cents_amt"  value=""/></p>
                </ol>
                    <submit><button>SUBMIT </button></submit>
                </form>

        '''
    else:
        dollar_amt = request.form['dollar_amt']
        cents_amt = request.form['cents_amt']
        if float(cents_amt) < 100:
            total = f"{dollar_amt}.{cents_amt}"
            new_amt_100x = float(total) * float(100)
            return f'''Dollar amount: {dollar_amt} <br>
                               cents: {cents_amt} <br>
                               total: {total} <br>
                         total * 100 = {new_amt_100x} '''
        else:
            return '''cents must be under 100, retry form
            <button> Please press your browsers back button and try again </button>'''


    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
