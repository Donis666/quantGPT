import gradio as gr
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import yfinance as yfin
import openai
yfin.pdr_override()

# Set your API key
openai.api_key = "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"
preset = "You now act as an agent to help me transform user's input to a formatted dictionary. The user should only request for financial stock market data. If it is not the case, you return a message 'ERROR'. If the user indeed ask for financial data, for example, give me the stock of apple in recent 60 days. Then you return a dictionary {'stock': 'AAPL', time: 60}.\n If no date information is found, then you set it by default to 60\n"

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





def plot_stock_gpt(prompt):
    prompt_to_gpt = preset + prompt
    response = generate_response(prompt_to_gpt)
    try:
        input_dict = eval(response)
        if (type(input_dict) != dict):
            gr.Error("invalid input! Try it again!")
    except:
        gr.Error("invalid input!")
    
    return plot_stock(input_dict['stock'], input_dict['time'])




def plot_stock(stock_name, time_period):
    # Fetch stock data
    end_date = pd.to_datetime('today')
    start_date = end_date - pd.to_timedelta(time_period, unit='D')
    stock_data = pdr.get_data_yahoo(stock_name, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))

    # Plot stock data
    fig, ax = plt.subplots()
    ax.plot(stock_data['Close'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Close Price')
    ax.set_title(f'{stock_name} Stock Prices for the Last {time_period} Days')
    ax.grid()

    # Save plot as an image
    fig.savefig('stock_plot.png', bbox_inches='tight')

    return 'stock_plot.png'



# Define Gradio input and output components
# inputs = [
#     gr.Textbox(label="Stock Name (e.g. AAPL)"),
#     gr.Slider(minimum=1, maximum=365, label="Time Period (Days)")
# ]

inputs = [gr.Textbox(label="input your requirements!")]

output = gr.Image(label="Stock Price Plot")

# Create the Gradio interface

iface = gr.Interface(
    fn=plot_stock_gpt,
    inputs=inputs,
    outputs=output,
    title="Stock Price Plotter",
    description="This is quantGPT! Try asking for financial data with natural language!",
    examples=[["give me the stock of apple in past 70 days"]]
)

# Launch the app
iface.launch()