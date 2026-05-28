import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# --- KONFIGURASI DASHBOARD ---
st.set_page_config(page_title="Auto Stock Screener", layout="wide")
st.title("📊 Stock Win Rate Backtester V2.1")
st.markdown("Mesin Backtest Kuantitatif - Alpha Project")

# --- DAFTAR SAHAM IDX ---
raw_tickers = (
"AADI,AALI,ABBA,ABDA,ABMM,ACES,ACRO,ACST,ADCP,ADES,ADHI,ADMF,ADMG,ADMR,ADRO,AEGS,AGAR,AGII,AGRO,AGRS,"
"AHAP,AIMS,AISA,AKKU,AKPI,AKRA,AKSI,ALDO,ALII,ALKA,ALMI,ALTO,AMAG,AMAN,AMAR,AMFG,AMIN,AMMN,AMMS,AMOR,"
"AMRT,ANDI,ANJT,ANTM,APEX,APIC,APII,APLI,APLN,ARCI,AREA,ARGO,ARII,ARKA,ARKO,ARMY,ARNA,ARTA,ARTI,ARTO,"
"ASBI,ASDM,ASGR,ASHA,ASII,ASJT,ASLC,ASLI,ASMI,ASPI,ASPR,ASRI,ASRM,ASSA,ATAP,ATIC,ATLA,AUTO,AVIA,AWAN,"
"AXIO,AYAM,AYLS,BABP,BABY,BACA,BAIK,BAJA,BALI,BANK,BAPA,BAPI,BATA,BATR,BAUT,BAYU,BBCA,BBHI,BBKP,BBLD,"
"BBMD,BBNI,BBRI,BBRM,BBSI,BBSS,BBTN,BBYB,BCAP,BCIC,BCIP,BDKR,BDMN,BEBS,BEEF,BEER,BEKS,BELI,BELL,BESS,"
"BEST,BFIN,BGTG,BHAT,BHIT,BIKA,BIKE,BIMA,BINA,BINO,BIPI,BIPP,BIRD,BISI,BJBR,BJTM,BKDP,BKSL,BKSW,BLES,"
"BLOG,BLTA,BLTZ,BLUE,BMAS,BMBL,BMHS,BMRI,BMSR,BMTR,BNBA,BNBR,BNGA,BNII,BNLI,BOAT,BOBA,BOGA,BOLA,BOLT,"
"BOSS,BPFI,BPII,BPTR,BRAM,BREN,BRIS,BRMS,BRNA,BRPT,BRRC,BSBK,BSDE,BSIM,BSML,BSSR,BSWD,BTEK,BTEL,BTON,"
"BTPN,BTPS,BUAH,BUDI,BUKA,BUKK,BULL,BUMI,BUVA,BVIC,BWPT,BYAN,CAKK,CAMP,CANI,CARE,CARS,CASA,CASH,CASS,"
"CBDK,CBMF,CBPE,CBRE,CBUT,CCSI,CDIA,CEKA,CENT,CFIN,CGAS,CHEK,CHEM,CHIP,CINT,CITA,CITY,CLAY,CLEO,CLPI,"
"CMNP,CMNT,CMPP,CMRY,CNKO,CNMA,CNTB,CNTX,COAL,COCO,COIN,COWL,CPIN,CPRI,CPRO,CRAB,CRSN,CSAP,CSIS,CSMI,"
"CSRA,CTBN,CTRA,CTTH,CUAN,CYBR,DAAZ,DADA,DART,DATA,DAYA,DCII,DEAL,DEFI,DEPO,DEWA,DEWI,DFAM,DGIK,DGNS,"
"DGWG,DIGI,DILD,DIVA,DKFT,DKHH,DLTA,DMAS,DMMX,DMND,DNAR,DNET,DOID,DOOH,DOSS,DPNS,DPUM,DRMA,DSFI,DSNG,"
"DSSA,DUCK,DUTI,DVLA,DWGL,DYAN,EAST,ECII,EDGE,EKAD,ELIT,ELPI,ELSA,ELTY,EMAS,EMDE,EMTK,ENAK,ENRG,ENVY,"
"ENZO,EPAC,EPMT,ERAA,ERAL,ERTX,ESIP,ESSA,ESTA,ESTI,ETWA,EURO,EXCL,FAPA,FAST,FASW,FILM,FIMP,FIRE,FISH,"
"FITT,FLMC,FMII,FOLK,FOOD,FORE,FORU,FPNI,FUJI,FUTR,FWCT,GAMA,GDST,GDYR,GEMA,GEMS,GGRM,GGRP,GHON,GIAA,"
"GJTL,GLOB,GLVA,GMFI,GMTD,GOLD,GOLF,GOLL,GOOD,GOTO,GOTOM,GPRA,GPSO,GRIA,GRPH,GRPM,GSMF,GTBO,GTRA,GTSI,"
"GULA,GUNA,GWSA,GZCO,HADE,HAIS,HAJJ,HALO,HATM,HBAT,HDFA,HDIT,HEAL,HELI,HERO,HEXA,HGII,HILL,HITS,HKMU,"
"HMSP,HOKI,HOME,HOMI,HOPE,HOTL,HRME,HRTA,HRUM,HUMI,HYGN,IATA,IBFN,IBOS,IBST,ICBP,ICON,IDEA,IDPR,IFII,"
"IFSH,IGAR,IIKP,IKAI,IKAN,IKBI,IKPM,IMAS,IMJS,IMPC,INAF,INAI,INCF,INCI,INCO,INDF,INDO,INDR,INDS,INDX,"
"INDY,INET,INKP,INOV,INPC,INPP,INPS,INRU,INTA,INTD,INTP,IOTF,IPAC,IPCC,IPCM,IPOL,IPPE,IPTV,IRRA,IRSX,"
"ISAP,ISAT,ISEA,ISSP,ITIC,ITMA,ITMG,JARR,JAST,JATI,JAWA,JAYA,JECC,JGLE,JIHD,JKON,JMAS,JPFA,JRPT,JSKY,"
"JSMR,JSPT,JTPE,KAEF,KAQI,KARW,KAYU,KBAG,KBLI,KBLM,KBLV,KBRI,KDSI,KDTN,KEEN,KEJU,KETR,KIAS,KICI,KIJA,"
"KING,KINO,KIOS,KJEN,KKES,KKGI,KLAS,KLBF,KLIN,KMDS,KMTR,KOBX,KOCI,KOIN,KOKA,KONI,KOPI,KOTA,KPIG,KRAS,"
"KREN,KRYA,KSIX,KUAS,LABA,LABS,LAJU,LAND,LAPD,LCGP,LCKM,LEAD,LFLO,LIFE,LINK,LION,LIVE,LMAS,LMAX,LMPI,"
"LMSH,LOPI,LPCK,LPGI,LPIN,LPKR,LPLI,LPPF,LPPS,LRNA,LSIP,LTLS,LUCK,LUCY,MABA,MAGP,MAHA,MAIN,MANG,MAPA,"
"MAPB,MAPI,MARI,MARK,MASB,MAXI,MAYA,MBAP,MBMA,MBSS,MBTO,MCAS,MCOL,MCOR,MDIA,MDIY,MDKA,MDKI,MDLA,MDLN,"
"MDRN,MEDC,MEDS,MEGA,MEJA,MENN,MERI,MERK,META,MFMI,MGLV,MGNA,MGRO,MHKI,MICE,MIDI,MIKA,MINA,MINE,MIRA,"
"MITI,MKAP,MKNT,MKPI,MKTR,MLBI,MLIA,MLPL,MLPT,MMIX,MMLP,MNCN,MOLI,MORA,MPIX,MPMX,MPOW,MPPA,MPRO,MPXL,"
"MRAT,MREI,MSIE,MSIN,MSJA,MSKY,MSTI,MTDL,MTEL,MTFN,MTLA,MTMH,MTPS,MTRA,MTSM,MTWI,MUTU,MYOH,MYOR,MYTX,"
"NAIK,NANO,NASA,NASI,NATO,NAYZ,NCKL,NELY,NEST,NETV,NFCX,NICE,NICK,NICL,NIKL,NINE,NIRO,NISP,NOBU,NPGF,"
"NRCA,NSSS,NTBK,NUSA,NZIA,OASA,OBAT,OBMD,OCAP,OILS,OKAS,OLIV,OMED,OMRE,OPMS,PACK,PADA,PADI,PALM,PAMG,"
"PANI,PANR,PANS,PART,PBID,PBRX,PBSA,PCAR,PDES,PDPP,PEGE,PEHA,PEVE,PGAS,PGEO,PGJO,PGLI,PGUN,PICO,PIPA,"
"PJAA,PJHB,PKPK,PLAN,PLAS,PLIN,PMJS,PMMP,PMUI,PNBN,PNBS,PNGO,PNIN,PNLF,PNSE,POLA,POLI,POLL,POLU,POLY,"
"POOL,PORT,POSA,POWR,PPGL,PPRE,PPRI,PPRO,PRAY,PRDA,PRIM,PSAB,PSAT,PSDN,PSGO,PSKT,PSSI,PTBA,PTDU,PTIS,"
"PTMP,PTMR,PTPP,PTPS,PTPW,PTRO,PTSN,PTSP,PUDP,PURA,PURE,PURI,PWON,PYFA,PZZA,RAAM,RAFI,RAJA,RALS,RANC,"
"RATU,RBMS,RCCC,RDTX,REAL,RELF,RELI,RGAS,RICY,RIGS,RIMO,RISE,RLCO,RMKE,RMKO,ROCK,RODA,RONY,ROTI,RSCH,"
"RSGK,RUIS,RUNS,SAFE,SAGE,SAME,SAMF,SAPX,SATU,SBAT,SBMA,SCCO,SCMA,SCNP,SCPI,SDMU,SDPC,SDRA,SEMA,SFAN,"
"SGER,SGRO,SHID,SHIP,SICO,SIDO,SILO,SIMA,SIMP,SINI,SIPD,SKBM,SKLT,SKRN,SKYB,SLIS,SMAR,SMBR,SMCB,SMDM,"
"SMDR,SMGA,SMGR,SMIL,SMKL,SMKM,SMLE,SMMA,SMMT,SMRA,SMRU,SMSM,SNLK,SOCI,SOFA,SOHO,SOLA,SONA,SOSS,SOTS,"
"SOUL,SPMA,SPRE,SPTO,SQMI,SRAJ,SRIL,SRSN,SRTG,SSIA,SSMS,SSTM,STAA,STAR,STRK,STTP,SUGI,SULI,SUNI,SUPA,"
"SUPR,SURE,SURI,SWAT,SWID,TALF,TAMA,TAMU,TAPG,TARA,TAXI,TAYS,TBIG,TBLA,TBMS,TCID,TCPI,TDPM,TEBE,TECH,"
"TELE,TFAS,TFCO,TGKA,TGRA,TGUK,TIFA,TINS,TIRA,TIRT,TKIM,TLDN,TLKM,TMAS,TMPO,TNCA,TOBA,TOOL,TOPS,TOSK,"
"TOTL,TOTO,TOWR,TOYS,TPIA,TPMA,TRAM,TRGU,TRIL,TRIM,TRIN,TRIO,TRIS,TRJA,TRON,TRST,TRUE,TRUK,TRUS,TSPC,"
"TUGU,TYRE,UANG,UCID,UDNG,UFOE,ULTJ,UNIC,UNIQ,UNIT,UNSP,UNTD,UNTR,UNVR,URBN,UVCR,VAST,VERN,VICI,VICO,"
"VINS,VISI,VIVA,VKTR,VOKS,VRNA,VTNY,WAPO,WBSA,WEGE,WEHA,WGSH,WICO,WIDI,WIFI,WIIM,WIKA,WINE,WINR,WINS,"
"WIRG,WMPP,WMUU,WOMF,WOOD,WOWS,WSBP,WSKT,WTON,YELO,YOII,YPAS,YULE,YUPI,ZATA,ZEUS,ZBRA,ZINC,ZONE,ZYRX,"
)
idx_tickers = sorted(list(set(t for t in raw_tickers.split(',') if t.strip())))

# --- UI ---
col1, col2 = st.columns(2)
with col1:
    ticker = st.selectbox("Select Ticker:", idx_tickers)
with col2:
    period = st.selectbox("Select Period:", ["1y", "2y", "3y", "5y", "max"])


# ============================================================
# FUNGSI UTAMA: HITUNG SEMUA INDIKATOR & SINYAL
# ============================================================
def run_backtest(ticker: str, period: str) -> pd.DataFrame | None:
    df = yf.Ticker(f"{ticker}.JK").history(period=period)

    if df.empty:
        st.error(f"Data untuk {ticker} tidak ditemukan.")
        return None

    df.index = df.index.tz_localize(None)

    # ----------------------------------------------------------
    # INDIKATOR DASAR
    # ----------------------------------------------------------
    df['SMA_5']       = df['Close'].rolling(5).mean()
    df['MA_50']       = df['Close'].rolling(50).mean()
    df['MA_200']      = df['Close'].rolling(200).mean()
    df['Value_Trx']   = df['Close'] * df['Volume']
    df['Resisten_20'] = df['High'].rolling(20).max()
    df['Support_20']  = df['Low'].rolling(20).min()

    # Bollinger Bands (20, 2)
    df['BB_MID']   = df['Close'].rolling(20).mean()
    df['BB_STD']   = df['Close'].rolling(20).std()
    df['BB_UPPER'] = df['BB_MID'] + 2 * df['BB_STD']
    df['BB_LOWER'] = df['BB_MID'] - 2 * df['BB_STD']
    df['BB_BW']    = (df['BB_UPPER'] - df['BB_LOWER']) / df['BB_MID']  # Bandwidth

    # EMA untuk BB MID filter
    df['EMA_10'] = df['Close'].ewm(span=10, adjust=False).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['EMA_50'] = df['Close'].ewm(span=50, adjust=False).mean()

    # Prev Low of last 5 bars (rolling min of Low over previous 5 candles, tidak termasuk hari ini)
    df['LLV_5'] = df['Low'].shift(1).rolling(5).min()   # prev llv("low", 5)
    df['LLV_1'] = df['Low'].shift(1)                    # prev llv("low", 1) = low kemarin

    # Data H+1 untuk evaluasi hasil
    df['High_Besok']        = df['High'].shift(-1)
    df['Cuan_Pct_Besok']    = ((df['High_Besok'] - df['Close']) / df['Close']) * 100

    # Filter minimum value transaksi 1 Miliar
    cond_val_1b = df['Value_Trx'] >= 1_000_000_000
    cond_val_5b = df['Value_Trx'] >= 5_000_000_000

    # ----------------------------------------------------------
    # SINYAL V1.1 — SMA5 Breakout Reversal
    # Candle H-1: merah, di bawah SMA5
    # Candle H-0: hijau, di atas SMA5
    # ----------------------------------------------------------
    cond_v11_h1 = (df['Close'].shift(1) < df['Open'].shift(1)) & \
                  (df['Close'].shift(1) < df['SMA_5'].shift(1))
    cond_v11_h0 = (df['Close'] > df['Open']) & \
                  (df['Close'] > df['SMA_5'])
    df['V1.1_Signal'] = cond_v11_h1 & cond_v11_h0 & cond_val_1b

    # ----------------------------------------------------------
    # SINYAL V1.2 — Pullback ke SMA5
    # H-2: naik tinggi (high/close H-3 >= 1.1)
    # H-1: hijau, di atas SMA5
    # H-0: merah/koreksi, masih di atas atau mendekati SMA5
    # ----------------------------------------------------------
    cond_v12_naik_tinggi = (df['High'].shift(2) / df['Close'].shift(3)) >= 1.10
    cond_v12_h1 = (df['Close'].shift(1) > df['SMA_5'].shift(1))
    cond_v12_h0 = (df['Close'] < df['Open']) & \
                  (df['Close'] >= df['SMA_5'] * 0.98) & \
                  (df['Close'] <= df['SMA_5'] * 1.05)
    df['V1.2_Signal'] = cond_v12_naik_tinggi & cond_v12_h1 & cond_v12_h0 & cond_val_1b

    # ----------------------------------------------------------
    # SINYAL V1.3 — Continuation / Breakout Resisten
    # 3 candle sebelumnya hijau & di atas SMA5
    # H-0: breakout di atas resisten 20 hari
    # ----------------------------------------------------------
    cond_v13_1 = (df['Close'].shift(1) > df['Open'].shift(1)) & (df['Close'].shift(1) > df['SMA_5'].shift(1))
    cond_v13_2 = (df['Close'].shift(2) > df['Open'].shift(2)) & (df['Close'].shift(2) > df['SMA_5'].shift(2))
    cond_v13_3 = (df['Close'].shift(3) > df['Open'].shift(3)) & (df['Close'].shift(3) > df['SMA_5'].shift(3))
    cond_v13_h0 = df['Close'] > df['Resisten_20'].shift(1)
    df['V1.3_Signal'] = cond_v13_1 & cond_v13_2 & cond_v13_3 & cond_v13_h0 & cond_val_1b

    # ----------------------------------------------------------
    # SINYAL V2.1 — Break SMA5 >10% + Value >5B (Reversal)
    # H-1: di bawah SMA5
    # H-0: hijau, break SMA5 minimal 10%, value >5B
    # ----------------------------------------------------------
    cond_v21_h1 = df['Close'].shift(1) < df['SMA_5'].shift(1)
    cond_v21_h0 = (df['Close'] > df['SMA_5']) & \
                  (((df['Close'] - df['SMA_5']) / df['SMA_5']) * 100 >= 10)
    df['V2.1_Signal'] = cond_v21_h1 & cond_v21_h0 & cond_val_5b

    # ----------------------------------------------------------
    # SINYAL V2.2 — Sideways Breakout +10% + Value >5B
    # Kondisi sideways: range 20 hari <= 10%
    # H-0: break SMA5 minimal 10%, value >5B
    # ----------------------------------------------------------
    cond_sideways = ((df['Resisten_20'].shift(1) - df['Support_20'].shift(1)) / df['Support_20'].shift(1)) <= 0.10
    df['V2.2_Signal'] = cond_sideways & cond_v21_h0 & cond_val_5b

    # ----------------------------------------------------------
    # SINYAL BB REVERSAL
    # Rumus: prev llv("Low",1) < BB_LOWER dan prev close < BB_LOWER
    #        close > BB_LOWER, volume > prev volume
    #        prev high < current high, current close > prev close
    # ----------------------------------------------------------
    bb_rev_h1_low_below  = df['LLV_1'] < df['BB_LOWER'].shift(1)           # low kemarin di bawah BBB
    bb_rev_h1_close_belo = df['Close'].shift(1) < df['BB_LOWER'].shift(1)  # close kemarin di bawah BBB
    bb_rev_h1_merah      = df['Close'].shift(1) < df['Open'].shift(1)       # candle kemarin merah
    bb_rev_h0_close_abov = df['Close'] > df['BB_LOWER']                     # close hari ini di atas BBB
    bb_rev_h0_hijau      = df['Close'] > df['Open']                          # candle hari ini hijau
    bb_rev_h0_vol        = df['Volume'] > df['Volume'].shift(1)              # volume lebih besar
    bb_rev_h0_hh         = df['High'] > df['High'].shift(1)                 # higher high
    bb_rev_h0_hc         = df['Close'] > df['Close'].shift(1)               # higher close
    df['BB_Rev_Signal'] = (
        bb_rev_h1_low_below  &
        bb_rev_h1_close_belo &
        bb_rev_h1_merah      &
        bb_rev_h0_close_abov &
        bb_rev_h0_hijau      &
        bb_rev_h0_vol        &
        bb_rev_h0_hh         &
        bb_rev_h0_hc         &
        cond_val_1b
    )

    # ----------------------------------------------------------
    # SINYAL BB MID (Pullback ke Bollinger Mid)
    # Rumus: close >= BB_MID*0.98 AND close <= BB_MID*1.02
    #        EMA10 > EMA20 > EMA50, BB Bandwidth >= 0.1
    #        close > BB_MID (sentuhan dari atas)
    # ----------------------------------------------------------
    bb_mid_naik_sebelum = (df['Close'].shift(1) > df['Open'].shift(1)) & \
                          (df['Low'].shift(1) > df['BB_MID'].shift(1))  # H-1 hijau, belum sentuh
    bb_mid_sentuh  = (df['Close'] < df['Open']) & \
                     (df['Close'] >= df['BB_MID'] * 0.98) & \
                     (df['Close'] <= df['BB_MID'] * 1.02)               # candle merah mendekati / menyentuh BB Mid
    bb_mid_ema     = (df['EMA_10'] > df['EMA_20']) & (df['EMA_20'] > df['EMA_50'])
    bb_mid_bw      = df['BB_BW'] >= 0.10                                # bandwidth cukup lebar
    bb_mid_above   = df['Close'] > df['BB_MID']                         # close masih di atas BB Mid
    df['BB_Mid_Signal'] = (
        bb_mid_naik_sebelum &
        bb_mid_sentuh       &
        bb_mid_ema          &
        bb_mid_bw           &
        bb_mid_above        &
        cond_val_1b
    )

    # ----------------------------------------------------------
    # SINYAL MA 50 (Pullback ke MA 50)  ← DIPISAH dari MA 200
    # Rumus: prev llv("low",5) > MA50 (5 candle sebelumnya tidak pernah tembus MA50)
    #        close >= MA50*0.99 AND close <= MA50*1.02
    #        MA50 > MA200 (uptrend), value > 1B
    # ----------------------------------------------------------
    ma50_uptrend     = df['MA_50'] > df['MA_200']
    ma50_llv_above   = df['LLV_5'] > df['MA_50'].shift(1)              # prev llv(5) > MA50 → belum pernah tembus
    ma50_close_range = (df['Close'] >= df['MA_50'] * 0.99) & \
                       (df['Close'] <= df['MA_50'] * 1.02)              # close di sekitar MA50
    ma50_merah       = df['Close'] < df['Open']                         # candle merah (buy on red)
    df['MA50_Signal'] = (
        ma50_uptrend   &
        ma50_llv_above &
        ma50_close_range &
        ma50_merah     &
        cond_val_1b
    )

    # ----------------------------------------------------------
    # SINYAL MA 200 (Pullback ke MA 200)  ← BARU, TERPISAH
    # Rumus: prev llv("low",5) > MA200
    #        close >= MA200*0.99 AND close <= MA200*1.02
    #        MA50 > MA200 (uptrend), value > 1B
    # ----------------------------------------------------------
    ma200_uptrend     = df['MA_50'] > df['MA_200']
    ma200_llv_above   = df['LLV_5'] > df['MA_200'].shift(1)
    ma200_close_range = (df['Close'] >= df['MA_200'] * 0.99) & \
                        (df['Close'] <= df['MA_200'] * 1.02)
    ma200_merah       = df['Close'] < df['Open']
    df['MA200_Signal'] = (
        ma200_uptrend    &
        ma200_llv_above  &
        ma200_close_range &
        ma200_merah      &
        cond_val_1b
    )

    return df


# ============================================================
# FUNGSI RENDER HASIL BACKTEST
# ============================================================
def display_results(df: pd.DataFrame, signal_col: str, title: str, extra_cols: dict = None):
    """
    extra_cols: dict { "Label Kolom": Series } — kolom tambahan spesifik per strategi
    """
    df_sig = df[df[signal_col] == True].copy()

    with st.expander(f"📘 {title}", expanded=True):
        if df_sig.empty:
            st.info(f"Sinyal '{title}' tidak muncul pada periode ini.")
            return

        # Kolom dasar
        ui = pd.DataFrame({
            "Tanggal"          : df_sig.index.strftime('%Y-%m-%d'),
            "Close"            : df_sig['Close'].round(0),
            "SMA 5"            : df_sig['SMA_5'].round(0),
            "Value (Miliar)"   : (df_sig['Value_Trx'] / 1e9).round(2),
            "Max Rise H+1 (%)" : df_sig['Cuan_Pct_Besok'].round(2),
        })

        # Kolom tambahan (misal MA50, BB_MID, dll.)
        if extra_cols:
            for label, series in extra_cols.items():
                ui[label] = series[df_sig.index].round(2).values

        # Tentukan win/lose
        ui['Status'] = np.where(ui['Max Rise H+1 (%)'] >= 1.0, "WIN ✅", "LOSE ❌")

        # Reorder: Status di kolom terakhir sudah benar
        total  = len(ui)
        wins   = (ui['Status'] == "WIN ✅").sum()
        wr     = wins / total * 100

        c1, c2, c3 = st.columns(3)
        c1.metric("Total Signal", total)
        c2.metric("Win (H+1 ≥1%)", wins)
        c3.metric("Win Rate", f"{wr:.1f}%")

        # Warnai baris
        def color_status(val):
            return "color: green; font-weight:bold" if "WIN" in val else "color: red;"

        styled = ui.style.map(color_status, subset=["Status"])
        st.dataframe(styled, use_container_width=True)


# ============================================================
# TOMBOL RUN
# ============================================================
if st.button(f"🚀 Run All Backtests for {ticker}"):
    with st.spinner(f"Menganalisis {ticker}..."):
        df_result = run_backtest(ticker, period)

    if df_result is not None:
        st.success(f"Data {ticker} berhasil diproses — {len(df_result)} candle.")
        st.markdown("---")

        # ── KELOMPOK 1: SMA 5 Strategies ──────────────────────
        st.subheader("📗 SMA 5 Strategies")
        display_results(df_result, 'V1.1_Signal', 'V1.1 — SMA5 Breakout Reversal')
        display_results(df_result, 'V1.2_Signal', 'V1.2 — Pullback ke SMA5')
        display_results(df_result, 'V1.3_Signal', 'V1.3 — Continuation / Break Resisten')

        st.markdown("---")

        # ── KELOMPOK 2: Breakout +10% ──────────────────────────
        st.subheader("📙 Breakout +10% Strategies")
        display_results(df_result, 'V2.1_Signal', 'V2.1 — Reversal Break SMA5 ≥10% + Value >5B')
        display_results(df_result, 'V2.2_Signal', 'V2.2 — Sideways Breakout ≥10% + Value >5B')

        st.markdown("---")

        # ── KELOMPOK 3: Bollinger Bands ────────────────────────
        st.subheader("📘 Bollinger Bands Strategies")
        display_results(
            df_result, 'BB_Rev_Signal',
            'BB Reversal — Bounce dari Lower Band',
            extra_cols={"BB Lower": df_result['BB_LOWER']}
        )
        display_results(
            df_result, 'BB_Mid_Signal',
            'BB MID — Pullback ke Middle Band',
            extra_cols={
                "BB Mid"   : df_result['BB_MID'],
                "BB BW"    : df_result['BB_BW'],
            }
        )

        st.markdown("---")

        # ── KELOMPOK 4: Moving Average ─────────────────────────
        st.subheader("📕 Moving Average Strategies")
        display_results(
            df_result, 'MA50_Signal',
            'MA 50 — First Touch Pullback (Uptrend)',
            extra_cols={"MA 50": df_result['MA_50'], "MA 200": df_result['MA_200']}
        )
        display_results(
            df_result, 'MA200_Signal',
            'MA 200 — First Touch Pullback (Uptrend)',
            extra_cols={"MA 50": df_result['MA_50'], "MA 200": df_result['MA_200']}
        )

