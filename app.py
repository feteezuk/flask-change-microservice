from flask import Flask
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





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
