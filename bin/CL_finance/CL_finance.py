import yfinance as yf
import pandas as pd


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


def is_valid(symbol: str) -> bool:
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
      if is_valid(symbol):
        symbol_history = yf.Ticker(symbol + '.SA').history(start=start_date, end=end_date, interval=interval)
        dataframes[symbol] = symbol_history

    return dataframes


### TODO: def get_portfolio_matrix([symb1, symb2, symb3, ...], priod in ['1d', '1mo', '1y']) ->  Matrix of the mean of the period
