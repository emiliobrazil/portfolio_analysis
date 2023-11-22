import yfinance as yf
import pandas as pd
import numpy as np

def valid_stocks() -> list:
  '''
    Retrieves a list of valid stock symbols from the Brazilian financial market.

    Returns:
        list: A list of valid stock symbols, representing companies traded on the 
        Brazilian stock exchange.
  '''
  return ['AALL34', 'AALR3', 'AAPL34', 'ABBV34', 'ABCB10', 'ABCB4', 'ABCP11', 'ABEV3', 'ABTT34', 'ACNB34',
          'ADHM3', 'AFLT3', 'AGRO3', 'AHEB3', 'AIGB34', 'ALMI11', 'ALPA3', 'ALPA4', 'ALSO3', 'ALUP11',
          'ALUP3', 'ALUP4', 'ALZR11', 'AMAR3', 'AMGN34', 'AMZO34', 'ANCR11B', 'ANIM3', 'APER3', 'AQLL11',
          'ARFI11B', 'ARMT34', 'ARNC34', 'ARZZ3', 'ATOM3', 'ATTB34', 'AXPB34', 'AZEV3', 'AZEV4', 'AZUL4',
          'B3SA3', 'BAHI3', 'BALM3', 'BALM4', 'BARI11', 'BAUH4', 'BAZA3', 'BBAS3', 'BBDC3', 'BBDC3', 'BBDC4',
          'BBFI11B', 'BBPO11', 'BBRC11', 'BBSE3', 'BBVJ11', 'BBYY34', 'BCFF11', 'BCIA11', 'BCRI11', 'BDLL4',
          'BEEF3', 'BEES3', 'BEES4', 'BERK34', 'BGIP3', 'BGIP4', 'BIIB34', 'BIOM3', 'BLAK34', 'BMEB3', 'BMEB4',
          'BMGB4', 'BMIN3', 'BMIN4', 'BMKS3', 'BMYB34', 'BNBR3', 'BNFS11', 'BOAC34', 'BOBR4', 'BOEI34', 'BONY34',
          'BOXP34', 'BPAC11', 'BPAC3', 'BPAC5', 'BPAN4', 'BPFF11', 'BPHA3', 'BPRP11', 'BRAP3', 'BRAP4', 'BRCR11',
          'BRFS3', 'BRGE11', 'BRGE12', 'BRGE6', 'BRIV3', 'BRIV4', 'BRKM3', 'BRKM5', 'BRPR3', 'BRSR3', 'BRSR5',
          'BRSR6', 'BSLI4', 'BTCR11', 'CAML3', 'CARE11', 'CATP34', 'CBEE3', 'CBOP11', 'CCRO3', 'CEAB3', 'CEBR3',
          'CEDO3', 'CEDO4', 'CEEB3', 'CEEB5', 'CEED3', 'CEOC11', 'CGAS3', 'CGAS5', 'CGRA3', 'CGRA4', 'CHVX34',
          'CIEL3', 'CLSC4', 'CMCS34', 'CMIG3', 'CMIG4', 'CNES11', 'COCA34', 'COCE3', 'COCE5', 'COGN3', 'COLG34',
          'COPH34', 'CORR4', 'COTY34', 'COWC34', 'CPFE3', 'CPLE3', 'CPLE6', 'CPTS11B', 'CRFB3', 'CRIV3', 'CRIV4',
          'CRPG5', 'CRPG6', 'CSAN3', 'CSCO34', 'CSMG3', 'CSNA3', 'CSRN3', 'CTGP34', 'CTKA4', 'CTNM3', 'CTNM4',
          'CTSA3', 'CTSA4', 'CTSH34', 'CTXT11', 'CVBI11', 'CVCB3', 'CVSH34', 'CXCE11B', 'CXRI11', 'CXTL11',
          'CYRE3', 'DAMT11B', 'DASA3', 'DDNB34', 'DEAI34', 'DHER34', 'DIRR3', 'DISB34', 'DMAC11', 'DOHL4',
          'DOMC11', 'DRIT11B', 'DTCY3', 'DUKB34', 'EALT3', 'EALT4', 'EBAY34', 'ECOR3', 'ECPR3', 'EDFO11B',
          'EDGA11', 'EGIE3', 'EKTR4', 'ELET3', 'ELET6', 'EMAE4', 'EMBR3', 'ENAT3', 'ENEV3', 'ENGI11', 'ENGI3',
          'ENGI4', 'ENMT3', 'ENMT4', 'EQTL3', 'ERPA11', 'ESTR4', 'ESUT11', 'ETER3', 'EUCA4', 'EURO11', 'EVEN3',
          'EXXO34', 'EZTC3', 'FAED11', 'FAMB11B', 'FCFL11', 'FCXO34', 'FDMO34', 'FDXB34', 'FESA3', 'FESA4', 'FHER3',
          'FIGS11', 'FIIB11', 'FIIP11B', 'FISC11', 'FIVN11', 'FIXX11', 'FLMA11', 'FLRP11', 'FLRY3', 'FMOF11', 'FMXB34',
          'FNAM11', 'FNOR11', 'FOFT11', 'FPAB11', 'FPNG11', 'FRAS3', 'FRIO3', 'FRTA3', 'FSLR34', 'FSPE11', 'FSRF11',
          'FSTU11', 'FTCE11B', 'FVPQ11', 'GDBR34', 'GEOO34', 'GEPA3', 'GEPA4', 'GESE11B', 'GFSA3', 'GGBR3', 'GGBR4',
          'GGRC11', 'GILD34', 'GMCO34', 'GOAU3', 'GOAU4', 'GOGL34', 'GOGL35', 'GOLL4', 'GPAR3', 'GPIV33', 'GPRO34',
          'GPSI34', 'GRLV11', 'GRND3', 'GSGI34', 'GSHP3', 'GTWR11', 'GUAR3', 'HABT11', 'HAGA3', 'HAGA4', 'HALI34',
          'HAPV3', 'HBOR3', 'HBTS5', 'HCRI11', 'HCTR11', 'HETA4', 'HFOF11', 'HGBS11', 'HGCR11', 'HGFF11', 'HGLG11',
          'HGPO11', 'HGRE11', 'HGRU11', 'HMOC11', 'HOME34', 'HONB34', 'HOOT4', 'HPQB34', 'HRDF11', 'HSHY34', 'HSML11',
          'HTMX11', 'HUSC11', 'HYPE3', 'IBFF11', 'IBMB34', 'IGBR3', 'INEP3', 'INEP4', 'IRBR3', 'IRDM11', 'ITLC34',
          'ITSA3', 'ITSA4', 'ITUB3', 'ITUB4', 'JBSS3', 'JFEN3', 'JHSF3', 'JNJB34', 'JOPA3', 'JOPA4', 'JPMC34', 'JPPC11',
          'JSLG3', 'JSRE11', 'KEPL3', 'KHCB34', 'KINP11', 'KLBN11', 'KLBN3', 'KLBN4', 'KMBB34', 'KNCR11', 'KNHY11',
          'KNIP11', 'KNRE11', 'KNRI11', 'LATR11B', 'LEVE3', 'LIGT3', 'LILY34', 'LIPR3', 'LMTB34', 'LOGG3', 'LOGN3',
          'LPSB3', 'LREN3', 'LUPA3', 'LUXM4', 'MACY34', 'MAPT3', 'MAXR11', 'MBRF11', 'MCDC34', 'MDIA3', 'MDLZ34',
          'MDTC34', 'MEAL3', 'MELI34', 'MERC4', 'METB34', 'MFII11', 'MGEL4', 'MGFF11', 'MGLU3', 'MILS3', 'MMMC34',
          'MMXM11', 'MNDL3', 'MNPR3', 'MOAR3', 'MOSC34', 'MOVI3', 'MRCK34', 'MRFG3', 'MRSA3B', 'MRSA6BF', 'MRVE3',
          'MSBR34', 'MSCD34', 'MSFT34', 'MSPA3', 'MTSA4', 'MULT3', 'MWET4', 'MXRF11', 'MYPK3', 'NCHB11', 'NEOE3',
          'NFLX34', 'NIKE34', 'NSLU11', 'NUTR3', 'NVHO11', 'ODPV3', 'OFSA3', 'OIBR3', 'OIBR4', 'ONEF11', 'ORCL34',
          'OSXB3', 'OUJP11', 'OULG11B', 'PABY11', 'PATC11', 'PATI3', 'PATI4', 'PDGR3', 'PEAB3', 'PEAB4', 'PEPB34',
          'PETR3', 'PETR4', 'PFIZ34', 'PFRM3', 'PGCO34', 'PINE4', 'PLAS3', 'PLRI11', 'PMAM3', 'PNVL3', 'POMO3', 'POMO4',
          'PORD11', 'POSI3', 'PPLA11', 'PQDP11', 'PRIO3', 'PRSN11B', 'PRSV11', 'PSSA3', 'PTBL3', 'PTNT4', 'QCOM34',
          'QUAL3', 'RADL3', 'RAIL3', 'RANI3', 'RAPT3', 'RAPT4', 'RBBV11', 'RBCB11', 'RBCO11', 'RBCO11', 'RBDS11',
          'RBED11', 'RBFF11', 'RBGS11', 'RBRD11', 'RBRF11', 'RBRP11', 'RBRR11', 'RBRY11', 'RBVA11', 'RBVO11', 'RCFA11',
          'RCRB11', 'RCRI11B', 'RCSL3', 'RCSL4', 'RDES11', 'RDNI3', 'RECT11', 'REDE3', 'REIT11', 'RENT3', 'RIGG34',
          'RNDP11', 'RNEW11', 'RNEW3', 'RNEW4', 'RNGO11', 'ROMI3', 'ROST34', 'RPAD3', 'RPAD5', 'RPAD6', 'RPMG3',
          'RSID3', 'RSPD11', 'RSUL4', 'SAAG11', 'SADI11', 'SAIC11B', 'SANB11', 'SANB3', 'SANB4', 'SAPR11', 'SAPR3',
          'SAPR4', 'SBSP3', 'SBUB34', 'SCAR3', 'SCHW34', 'SCPF11', 'SDIL11', 'SEER3', 'SGPS3', 'SHDP11B', 'SHOP11',
          'SHOW3', 'SHPH11', 'SHUL4', 'SLBG34', 'SLCE3', 'SLED3', 'SLED4', 'SMTO3', 'SNSY5', 'SOND5', 'SOND6', 'SPTW11',
          'SQIA3', 'SSFO34', 'STBP3', 'SUZB3', 'TAEE11', 'TAEE3', 'TAEE4', 'TASA3', 'TASA4', 'TBOF11', 'TCSA3', 'TECN3',
          'TEKA4', 'TELB3', 'TELB4', 'TEND3', 'TEXA34', 'TFOF11', 'TGAR11', 'TGMA3', 'TGTB34', 'THRA11', 'TMOS34', 'TOTS3',
          'TPIS3', 'TRIS3', 'TRNT11', 'TRPL3', 'TRPL4', 'TRVC34', 'TSLA34', 'TSNC11', 'TUPY3', 'TXRX4', 'UBSG34', 'UCAS3',
          'UGPA3', 'UNIP3', 'UNIP5', 'UNIP6', 'UPAC34', 'UPSS34', 'USBC34', 'USIM3', 'USIM5', 'USIM6', 'USSX34', 'VALE3',
          'VAMO3', 'VERE11', 'VERZ34', 'VGIR11', 'VILG11', 'VISA34', 'VISC11', 'VIVA3', 'VIVR3', 'VIVT3', 'VLID3', 'VLOE34',
          'VRTA11', 'VSHO11', 'VSPT3', 'VTLT11', 'VULC3', 'WALM34', 'WEGE3', 'WFCO34', 'WHRL3', 'WHRL4', 'WLMM3', 'WLMM4',
          'WPLZ11', 'WTSP11B', 'WUNI34', 'XPCM11', 'XPHT11', 'XPIN11', 'XPLG11', 'XRXB34', 'YCHY11', 'YDUQ3']


def is_valid_stock(symbol: str) -> bool:
  """
  input:
      symbol: a str that represents a stock.
  output:
      bol: True if the symbol is a brazilian stock that is valid.
  """
  if symbol in valid_stocks():
    return True
  else:
    print(f'Stock {symbol} not found no B3 or may have been delisted.')
    return False
    
    
def history(symbols: list, start_date: str, end_date: str, interval: str):
    """
    input:
        symbols: A list of str that represent the stocks to recover the history
        start_date: Time object that represent the first day of the historical data. 
        	    Format: "YYYY-MM-DD"
        end_date: Time object that represent the last day of the historical data. 
        	  Format: "YYYY-MM-DD"
        interval: the interval of the historical: {1d, 5d, 1wk, 1mo, 3mo, 1y}    
    output:
        dataframes: List of Pandas DataFrames, where each DataFrame corresponds to the historical data for a valid stock in symbols
    """
    dataframes = {}
    for symbol in symbols:
      if is_valid_stock(symbol):
        symbol_history = yf.Ticker(symbol + '.SA').history(start=start_date, end=end_date, interval=interval)
        dataframes[symbol] = symbol_history

    return dataframes


class MeanPriceMatrix:
  """
    A class for calculating mean price matrices based on financial data.

    Parameters:
    - symbols (list): List of stock symbols.
    - start_date (str): Start date for the analysis.
    - end_date (str): End date for the analysis.
    - period (str): Analysis period ('1d' for daily, '1mo' for monthly, '1y' for yearly).

    Attributes:
    - get_portifolio_matrix (numpy.ndarray): Matrix of portfolio prices based on the selected period.
  """
  def __init__(self, symbols: list, start_date, end_date, period: str):
    """
      Initializes the MeanPriceMatrix object.

      If the period is '1d', get_portifolio_matrix will be set to the result of matrix_daily_price.
      If the period is '1mo', get_portifolio_matrix will be set to the result of matrix_monthly_price.
      If the period is '1y', get_portifolio_matrix will be set to the result of matrix_yearly_price.
    """
    self.symbols = symbols
    self.start_date = start_date
    self.end_date = end_date
    self.period = period

    if self.period == '1d':
      self.get_portifolio_matrix = self.matrix_daily_price(self.start_date, self.end_date)
    elif self.period == '1mo':
      self.get_portifolio_matrix = self.matrix_monthly_price(self.start_date, self.end_date)
    elif self.period == '1y':
      self.get_portifolio_matrix = self.matrix_yearly_price(self.start_date, self.end_date)


  def get_high_matrix(self, start_date, end_date):
    high_data = pd.DataFrame()
    for symbol in self.symbols:
      data = yf.Ticker(symbol +'.SA').history(start= start_date, end= end_date)
      high_data[symbol] = data['High']
    high_matrix = high_data.to_numpy()
    return high_matrix


  def get_low_matrix(self, start_date, end_date):
    low_data = pd.DataFrame()
    for symbol in self.symbols:
      data = yf.Ticker(symbol +'.SA').history(start= start_date, end= end_date)
      low_data[symbol] = data['Low']
    low_matrix = low_data.to_numpy()
    return low_matrix


  def matrix_daily_price(self, start_date, end_date):
    """
      Calculates the daily price matrix based on the high and low matrices.

      Parameters:
      - start_date (str): Start date for the data retrieval.
      - end_date (str): End date for the data retrieval.

      Returns:
      - numpy.ndarray: Daily price matrix.
    """
    high_matrix = self.get_high_matrix(start_date, end_date)
    low_matrix = self.get_low_matrix(start_date, end_date)
    sum_matrix = high_matrix + low_matrix
    result_matrix = np.multiply(0.5, sum_matrix)
    return result_matrix


  def mean_monthly_price(self, start_date: str, end_date: str):
    matrix = self.matrix_daily_price(start_date, end_date)
    mean_monthly = np.mean(matrix, axis=0)
    return mean_monthly


  def matrix_monthly_price(self, start_date: str, end_date: str):
    """
      Calculates the monthly price matrix based on the mean monthly price matrix.

      Parameters:
      - start_date (str): Start date for the data retrieval.
      - end_date (str): End date for the data retrieval.

      Returns:
      - numpy.ndarray: Monthly price matrix.
    """
    months_info = self.get_monthly_date_ranges(start_date, end_date)
    number_of_months = len(months_info)
    matrix = np.zeros((number_of_months, len(self.symbols)))
    for i, (first_day, last_day) in enumerate(months_info):
        matrix[i, :] = self.mean_monthly_price(first_day, last_day)
    return matrix

  
  def years(self):
    shape = self.matrix_monthly_price(self.start_date, self.end_date).shape
    years = []
    for i in range(0, shape[0], 12):
      year = self.matrix_monthly_price(self.start_date, self.end_date)[i:i+12, :len(self.symbols)]
      years.append(year)
    return years


  def mean_yearly_price(self, year_matrix):
    mean_yearly = np.mean(year_matrix, axis=0)
    return mean_yearly
    

  def matrix_yearly_price(self, start_date, end_date):
    """
      Calculates the yearly price matrix based on the mean yearly price matrix.

      Parameters:
      - start_date (str): Start date for the data retrieval.
      - end_date (str): End date for the data retrieval.

      Returns:
      - numpy.ndarray: Yearly price matrix.
    """
    matrix = np.zeros((len(self.years()), len(self.symbols)))
    for year in range(0, len(self.years())):
      matrix[year, :] = self.mean_yearly_price(self.years()[year])
    return matrix


  def get_monthly_date_ranges(self, start_date: str, end_date: str):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    all_monthly_dates = []
    current_date = start_date.replace(day=1)
    while current_date <= end_date:
        first_day_of_month = current_date
        last_day_of_month = current_date + pd.offsets.MonthEnd(0)
        all_monthly_dates.append((first_day_of_month, last_day_of_month))
        current_date = last_day_of_month + pd.DateOffset(days=1)
    return all_monthly_dates


def test():
  syb = 'PETR4'
  print(f"{syb} is valid? {is_valid_stock(syb)}")
  
  print(history([syb], "2020-10-01", "2023-10-21", '1mo'))
  
  matrix_syb = MeanPriceMatrix([syb, 'MGLU3', 'MWET4'], "2020-10-01", "2023-10-21", '1mo')
  print(matrix_syb.get_portifolio_matrix)

if __name__ == '__main__':
    test()
