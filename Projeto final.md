# Monte Carlo simulation para finanças
## Requerimento:

1. Biblioteca em Python que dado um portifolio de ações:
	1. calcula o risco e possiveis retornos usando uma janela de tempo especificada.
	2. interpola os valores usando splines
	3. cria representações gráficas
	4. (Bonus) Encontrar a combinação otima de quantidades de cada ação no portifolio que minimiza o risco ou maximiza o ganho
2. Inetrface grafica com o usuario que permita:
	1. criar, salvar e carregar portifolios
	2. selecionar ações do mercado brasileiro e mostrar o historico de tranzaçoes dos ultimos 3 messes
	3. exibir o resultado da biblioteca do item 1

### Exemplo de portifolio:
(SYMBOL, Quntidade)
ex: [('PETR4', 1000), ('VALE3', 5000), ('ITUB4', 2000), ('BBDC4', 1000), ('ABEV3', 3000)]

## Recursos:
https://pypi.org/project/yfinance/ 
https://docs.scipy.org/doc/scipy/reference/stats.qmc.html#quasi-monte-carlo
https://docs.scipy.org/doc/scipy/reference/interpolate.html#d-splines
https://www.investopedia.com/terms/m/montecarlosimulation.asp
https://www.portfoliovisualizer.com/monte-carlo-simulation
https://www.youtube.com/watch?v=vcdUP5hKGWo
#### Extras
https://www.sofi.com/learn/content/monte-carlo-simulation/
https://www.investopedia.com/articles/investing/112514/monte-carlo-simulation-basics.asp
https://www.investopedia.com/terms/m/montecarlosimulation.asp
https://sas.uwaterloo.ca/~dlmcleis/s906/chapt1-6.pdf
## Ações do mercado brasileiro

brazilian_stocks = 
    'PETR4', 'VALE3', 'ITUB4', 'BBDC4', 'ABEV3',
    'WEGE3', 'BBAS3', 'MGLU3', 'SUZB3',   'ALPA4', 'ALUP11', 
    'ALUP3', 'ALUP4', 'ANIM3', 'ARZZ3','ATMP3', 'ATOM3', 
    'AZEV3', 'BIDI11', 'BIDI3', 'BIDI4', 'BOBR3', 'BOBR4', 
    'BOVA11', 'BPAC3', 'BPAN4', 'BRAP4',  'BEEF3', 'BPAC11', 'BRAP3', 'BRKM3', 'CCRO3', 'CGRA3',
    'COGN3', 'CPLE6', 'CSAN3', 'CVCB3', 'CYRE3', 'ECOR3',
    'EGIE3', 'ELET3', 'ELET6', 'EMBR3', 'ENBR3', 'EQTL3',
    'FLRY3', 'GGBR3', 'GOAU3', 'GOLL3', 'HAPV3', 'HGTX3',
    'IGTA3', 'IRBR3', 'ITSA3', 'JHSF3', 'KLBN4', 'LAME3',
    'LCAM3', 'LREN3', 'MGLU3', 'MRFG3', 'MRVE3', 'MULT3',
    'NATU3', 'PCAR4', 'PETR3', 'QUAL3', 'RADL3', 'RAIL3',
    'RENT3', 'SANB3', 'SAPR11', 'SBSP3', 'SMLS3', 'SUZB3',
    'TAEE3', 'TIMP3', 'TOTS3', 'UGPA3', 'USIM3', 'VIVT3',
    'VVAR3', 'WEGE3', 'YDUQ3', 'ABEV3', 'AZUL4', 'B3SA3', 
    'BBAS3', 'BBDC3', 'BBDC4',
    'BBSE3', 'BRAP4', 'BRDT3', 'BRFS3', 'BRKM5', 'BRML3',
    'B3SA3', 'CCRO3', 'CIEL3', 'CMIG4', 'COGN3', 'CPFE3',
    'CRFB3', 'CSAN3', 'CSNA3', 'CVCB3', 'CYRE3', 'ECOR3',
    'EGIE3', 'ELET3', 'ELET6', 'EMBR3', 'ENBR3', 'EQTL3',
    'FLRY3', 'GGBR4', 'GOAU4', 'GOLL4', 'HAPV3', 'HGTX3',
    'IGTA3', 'IRBR3', 'ITSA4', 'ITUB3', 'ITUB4', 'JBSS3',
    'KLBN11', 'LAME4', 'LREN3', 'MGLU3', 'MRFG3', 'MRVE3',
    'MULT3', 'NATU3', 'PCAR3', 'PETR3', 'PETR4', 'QUAL3',
    'RADL3', 'RAIL3', 'RENT3', 'SANB11', 'SBSP3', 'SMLS3',
    'SUZB3', 'TAEE11', 'TIMP3', 'TOTS3', 'UGPA3', 'USIM5',
    'VALE3', 'VIVT3', 'VIVT4', 'VVAR3', 'WEGE3', 'YDUQ3',
    'BRFS3', 'BRKM5', 'BRML3', 'BRPR3', 'BRSR3', 'BRSR6',
    'BSEV3', 'CAMB3', 'CCPR3', 'CEAB3', 'CEAB5', 'CEAB6',
    'CESP3', 'CESP5', 'CESP6', 'CGAS3', 'CGAS5', 'CGRA3',
    'CGRA4', 'CIEL3', 'CLSC4', 'CMIG4', 'CMIG4', 'CMIGB4',
    'CMIGB6', 'CMIGC6', 'CNTO3', 'COGN3', 'CPFE3', 'CPLE3',
    'CPLE6', 'CPRE3', 'CRFB3', 'CSAB3', 'CSAB4', 'CSAN3',
    'CSRN3', 'CSRN5', 'CSRN6', 'CTKA3', 'CTKA4', 'CTNM3',
    'CTNM4', 'CVCB3', 'CYRE3', 'DASA3', 'DIRR3', 'DIRR6',
    'DMMO3', 'DMMO4', 'DOHL3', 'DOHL4', 'DTEX3', 'EALT4',
    'ECOR3', 'ECOR4', 'ECPG3', 'ECPG4', 'EEEL3', 'EEEL4',
    'EGIE3', 'ELEK3', 'ELEK4', 'ELET3', 'ELET6', 'ELPL3',
    'ELPL4', 'EMAE4', 'EMBR3', 'ENBR3', 'ENMA3', 'ENMA6',
    'ENMT3', 'ENMT4', 'EQPA3', 'EQPA5', 'EQPA6', 'EQTL3',
    'ESTR3', 'ESTR4', 'ETER3', 'EUCA4', 'EVEN3', 'EZZE',
    'FESA3', 'FESA4', 'FHER3', 'FJTA4', 'FLRY3', 'FRAS3',
    'FRIO3', 'GEPA3', 'GEPA4', 'GFSA3', 'GFSA3B', 'GGBR3',
    'GOAU3', 'GOAU4', 'GOGL34', 'GOLL3', 'GPAR3', 'GPIV33',
    'GPIV4', 'GRND3', 'GSHP3', 'GSHP4', 'GUAR3', 'GUAR4',
    'GUAR4B', 'HAGA4', 'HAPV3', 'HBTS5', 'HETA4', 'HGTX3',
    'HYPE3', 'IDNT3', 'IDVL3', 'IGBR3', 'IGBR5', 'IGBR6',
    'IGTA3', 'IGTA3B', 'INHA3', 'INHA4', 'INSC3', 'IRBR3',
    'IRBR3B', 'IRBR3C', 'ITSA3', 'ITSA4', 'ITSA4B', 'ITUB3',
    'ITUB3B', 'ITUB4', 'ITUB4B', 'JBSS3', 'JFEN3', 'JHSF3',
    'JOPA3', 'JOPA4', 'JSLG3', 'KEPL3', 'KEPL4', 'KLBN11',
    'KLBN3', 'KLBN4', 'LAME3', 'LAME4', 'LATM11', 'LBRN3',
    'LBRN5', 'LBRN6', 'LEVE3', 'LIGT3', 'LINX3', 'LLIS3',
    'LOGG3', 'LOGN3', 'LOGN11', 'LPSB3', 'LREN3', 'LUPA3',
    'LUPA4', 'LWSA3', 'LWSA3B', 'LXRE3', 'MACY34', 'MAGG3',
    'MAGS3', 'MALL11', 'MALL3', 'MALL4', 'MAPT3', 'MAPT4',
    'MDIA3', 'MDNE3', 'MDNE4', 'MGLU3', 'MILS3', 'MLAS3',
    'MMXM3', 'MMXM11', 'MOAR3', 'MOAR4', 'MOVI3', 'MRFG3',
    'MRVE3', 'MRVE3B', 'MTIG4', 'MTRE3', 'MTSA3', 'MTSA4',
    'MULT3', 'MYPK3', 'N1CE34', 'NEOE3', 'NEOE4', 'NEOE4B',
    'NORD3', 'NRTQ3', 'NUTR3', 'ODER3', 'ODER4', 'OMGE3',
    'OMGE3B', 'ORPD3', 'OSXB3', 'OSXB3B', 'OTRK3', 'P1GG34',
    'PAES3', 'PAES4', 'PARD3', 'PARD3B', 'PATI3', 'PATI4',
    'PATI4B', 'PCAR3', 'PCAR4', 'PCAR5', 'PCAR5B', 'PCAR6',
    'PCAR6B', 'PDGR3', 'PETR3', 'PETR4', 'PETR4B', 'PFIZ34',
    'PFRM3', 'PFRM3B', 'PINE4', 'PINE4B', 'PLAS3', 'PLAS3B',
    'PLPL3', 'PLPL4', 'PLPL4B', 'PLRI11', 'PMAM3', 'PMAM4',
    'PMAM4B', 'PNVL3', 'PNVL4', 'PNVL4B', 'POWE3', 'PPLA11',
    'PPLA3', 'PPLA4', 'PPLA4B', 'PPLA4C', 'PRBC3', 'PRBC4',
    'PRBC4B', 'PSSA3', 'PTBL3', 'PTBL3B', 'PTNT3', 'PTNT4',
    'PTNT4B', 'QUAL3', 'RADL3', 'RAIL3', 'RAIL4', 'RAIL4B',
    'RAPT3', 'RAPT4', 'RAPT4B', 'RCSL3', 'RCSL4', 'RCSL4B',
    'RDNI3', 'RDNI3B', 'RDOR3', 'RDOR4', 'RDOR4B', 'REDE3',
    'REDE4', 'REDE4B', 'RENT3', 'RNEW11', 'RNEW3', 'RNEW4',
    'RNEW4B', 'RSID3', 'RSID3B', 'RSPD3', 'RSPD4', 'RSPD4B',
    'RSUL4', 'S3SC3', 'SAPR3', 'SAPR4', 'SAPR4B', 'SAPR4C',
    'SBSP3', 'SEER3', 'SHOW3', 'SHOW4', 'SHUL4', 'SHUL4B',
    'SHUL4C', 'SLCE3', 'SLCE4', 'SLED3', 'SLED4', 'SLED4B',
    'SMLS3', 'SMLS3B', 'SMTO3', 'SOMA3', 'SOMA4', 'SOMA4B',
    'SPRI3', 'SPRI5', 'SPRI6', 'STBP3', 'STBP3B', 'STKF3',
    'STKF4', 'STKF4B', 'STTR3', 'STTR4', 'STTR4B', 'SULA11',
    'SULA3', 'SULA4', 'SULA4B', 'SULA4C', 'SULA4D', 'SULA4E',
    'TASA3', 'TASA4', 'TASA4B', 'TCNO3', 'TCNO4', 'TECN3',
    'TEKA3', 'TEKA4', 'TEKA4B', 'TEND3', 'TESA3', 'TESA4',
    'TESA4B', 'TGMA3', 'TGMA3B', 'TGMA4', 'TGMA4B', 'TORD3',
    'TORD3B', 'TOYB3', 'TOYB3B', 'TOYB4', 'TOYB4B', 'TPIS3',
    'TPIS3B', 'TRIS3', 'TRIS4', 'TRIS4B', 'TRPL3', 'TRPL4',
    'TRPL4B', 'TSLA34', 'TSLA35', 'TUPY3', 'TUPY4', 'TXRX3',
    'TXRX4', 'UCAS3', 'UCAS4', 'UGPA3', 'UGPA3B', 'UNIP3',
    'UNIP5', 'UNIP6', 'UPAC33', 'UPAC34', 'UPSS34', 'URPR11',
    'USIM3', 'USIM3B', 'USIM5', 'USIM5B', 'USIM6', 'USIM6B',
    'USIN11', 'USIN3', 'USIN4', 'USIN4B', 'UTEC34', 'VALE3',
    'VCPA3', 'VCPA4', 'VEVE3', 'VINE3', 'VIVO3', 'VIVO4',
    'VIVT3', 'VIVT4', 'VLID3', 'VLID4', 'VNET3', 'VNET4',
    'VPTA3', 'VPTA4', 'VPTA4B', 'VSPT3', 'VSPT4', 'VSPT4B',
    'VULC3', 'VULC4', 'VULC4B', 'VVAR11', 'WEGE3', 'WHRL3',
    'WHRL4', 'WHRL4B', 'WIZS3', 'WIZS3B', 'WSON33', 'WUNI11',
    'WUNI3', 'WUNI5', 'WUNI6', 'YBRA3', 'YBRA4',
