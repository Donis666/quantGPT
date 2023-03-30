import openai

# Set your API key
openai.api_key = "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"

def generate_response(prompt, model="text-davinci-003", max_tokens=100):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

preset = "You now act as an agent to help me transform user's input to a formatted dictionary. The user should only request for financial stock market data. If it is not the case, you return a message 'ERROR'. If the user indeed ask for financial data, for example, give me the stock of apple in recent 60 days. Then you return a dictionary {'stock': 'AAPL', time: 60}.\n If no date information is found, then you set it by default to 60\n"


# Test the function with a prompt
user_input = "give me the stock of apple in past 70 days"
response = generate_response(preset + user_input)
try:
    input_dict = eval(response)
    print(type(input_dict))
    print(type(input_dict['stock']))
    print(type(input_dict['time']))
except:
    print("error!")


user_input = "give me the stock of google in past 70 days"
response = generate_response(preset + user_input)
try:
    input_dict = eval(response)
    print(type(input_dict))
    print(type(input_dict['stock']))
    print(type(input_dict['time']))
except:
    print("error!")