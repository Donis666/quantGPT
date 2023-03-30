class Algorithm:
    """
    Expect the data to be a pandas data frame with datetime index 
    so that I could access to the data through datatime index;
    let's first target at being able to implement a SMA strategy 
    
    """
    def __init__(self) -> None:
        self.startDate = ''
        self.endDate= ''
        self.tickers = []
        self.data = self.getData()
        pass 

    def setHolding(self, ticker:str, weight):
        pass 

    def Liquidate(self, ticker:str):
        pass 

    def onData(self):
        # should be able to access to the current price
        pass 

    def trade(self):
        # iterate through rows, execute the on data;
        pass 

    def getData(self, startDate, endDate, tickers):
        # returns a pandas dataframe 
        # with columns as tickers 
        # indexing from start_date to end_date 
        pass