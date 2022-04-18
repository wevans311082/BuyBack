import sqlite3
from sqlite3 import Error
from urllib.request import Request
from re import sub
from bs4 import BeautifulSoup
import re
import requests


def get_prices(itemid):
    url = "https://api.evemarketer.com/ec/marketstat?usesystem=30000142&typeid=" + str(itemid)
    headers = {'User-Agent': 'Mozilla/5.0'}
    request = Request(url, headers=headers)
    response = requests.get(url).text
    xmldoc = response
    content = BeautifulSoup(xmldoc, features='html.parser')
    avg = content.find_all("min")
    value_str = avg[1]
    value2 = str(value_str).replace('<min>', '')
    value = str(value2).replace('</min>', '')
    return float(value)


def get_min_prices(min):
    list_of_minerals = [
        "34", "Tritanium",
        "35", "Pyerite",
        "36", "Mexallon",
        "37", "Isogen",
        "38", "Nocxium",
        "39", "Zydrine",
        "40", "Megacyte",
        "11399", "Morphite",
        "16272", "Heavy Water",
        "16273", "Liquid Ozone",
        "16274", "Helium Isotopes",
        "17887", "Oxygen Isotopes",
        "17888", "Nitrogen Isotopes",
        "17889", "Hydrogen Isotopes",
        "16275", "Strontium Clathrates",
        "16633", "Hydrocarbons",
        "16634", "Atmospheric Gases",
        "16635", "Evaporite Deposits",
        "16636", "Silicates",
        "16637", "Tungsten",
        "16638", "Titanium",
        "16639", "Scandium",
        "16640", "Cobalt",
        "16641", "Chromium",
        "16642", "Vanadium",
        "16643", "Cadmium",
        "16644", "Platinum",
        "16646", "Mercury",
        "16647", "Caesium",
        "16648", "Hafnium",
        "16649", "Technetium",
        "16650", "Dysprosium",
        "16651", "Neodymium",
        "16652", "Promethium",
        "16653", "Thulium",
        "28694", "Amber Mykoserocin",
        "28695", "Azure Mykoserocin",
        "28696", "Celadon Mykoserocin",
        "28697", "Golden Mykoserocin",
        "28698", "Lime Mykoserocin",
        "28699", "Malachite Mykoserocin",
        "28700", "Vermillion Mykoserocin",
        "28701", "Viridian Mykoserocin",
        "25268", "Amber Cytoserocin",
        "25279", "Azure Cytoserocin",
        "25275", "Celadon Cytoserocin",
        "25277", "Lime Cytoserocin",
        "25276", "Malachite Cytoserocin",
        "25278", "Vermillion Cytoserocin",
        "25274", "Viridian Cytoserocin",
        "30375", "Fullerite-C28",
        "30376", "Fullerite-C32",
        "30377", "Fullerite-C320",
        "30370", "Fullerite-C50",
        "30378", "Fullerite-C540",
        "30371", "Fullerite-C60",
        "30372", "Fullerite-C70",
        "30373", "Fullerite-C72",
        "30374", "Fullerite-C84"
    ]
    item = list_of_minerals.index(min)
    price = get_prices(list_of_minerals[item - 1])
#   print(min + ":" + str(price))
    return price


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_minerals(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM baselinecsv")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def col_names(conn):

        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info('baselinecsv')")
        data = cursor.fetchall()
        return [i[1] for i in data]



def get_value_from_ore(conn,ore,mineral):
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    query = "SELECT * FROM baselinecsv WHERE ore=='" + ore + "'"
#    print(query)
    cur.execute(query)
    r = cur.fetchone()
    amount = r[mineral]
    return amount



def get_all_minerals_in_ore(conn,ore,amount):
    base_reprocess_rate = 0.75
    #get amount in the ore
    amount_Tritanium = get_value_from_ore(conn, ore, "Tritanium")
    amount_Pyerite = get_value_from_ore(conn, ore, "Pyerite")
    amount_Mexallon = get_value_from_ore(conn, ore, "Mexallon")
    amount_Isogen = get_value_from_ore(conn, ore, "Isogen")
    amount_Nocxium = get_value_from_ore(conn, ore, "Nocxium")
    amount_Zydrine = get_value_from_ore(conn, ore, "Zydrine")
    amount_Megacyte = get_value_from_ore(conn, ore, "Megacyte")
    amount_Morphite = get_value_from_ore(conn, ore, "Morphite")
    amount_HeavyWater = get_value_from_ore(conn, ore, "HeavyWater")
    amount_LiquidOzone = get_value_from_ore(conn, ore, "LiquidOzone")
    amount_HeliumIsotopes = get_value_from_ore(conn, ore, "HeliumIsotopes")
    amount_StrontiumClathrates = get_value_from_ore(conn, ore, "StrontiumClathrates")
    amount_Hydrocarbons = get_value_from_ore(conn, ore, "Hydrocarbons")
    amount_AtmosphericGases = get_value_from_ore(conn, ore, "AtmosphericGases")
    amount_EvaporiteDeposits = get_value_from_ore(conn, ore, "EvaporiteDeposits")
    amount_Silicates = get_value_from_ore(conn, ore, "Silicates")
    amount_Tungsten = get_value_from_ore(conn, ore, "Tungsten")
    amount_Titanium = get_value_from_ore(conn, ore, "Titanium")
    amount_Scandium = get_value_from_ore(conn, ore, "Scandium")
    amount_Cobalt = get_value_from_ore(conn, ore, "Cobalt")
    amount_Chromium = get_value_from_ore(conn, ore, "Chromium")
    amount_Vanadium = get_value_from_ore(conn, ore, "Vanadium")
    amount_Cadmium = get_value_from_ore(conn, ore, "Cadmium")
    amount_Platinum = get_value_from_ore(conn, ore, "Platinum")
    amount_Mercury = get_value_from_ore(conn, ore, "Mercury")
    amount_Caesium = get_value_from_ore(conn, ore, "Caesium")
    amount_Hafnium = get_value_from_ore(conn, ore, "Hafnium")
    amount_Technetium = get_value_from_ore(conn, ore, "Technetium")
    amount_Dysprosium = get_value_from_ore(conn, ore, "Dysprosium")
    amount_Neodymium = get_value_from_ore(conn, ore, "Neodymium")
    amount_Promethium = get_value_from_ore(conn, ore, "Promethium")
    amount_Thulium = get_value_from_ore(conn, ore, "Thulium")
    amount_OxygenIsotopes = get_value_from_ore(conn, ore, "OxygenIsotopes")
    amount_NitrogenIsotopes = get_value_from_ore(conn, ore, "NitrogenIsotopes")
    amount_HydrogenIsotopes = get_value_from_ore(conn, ore, "HydrogenIsotopes")

    print("AMOUNTS IN THE ORE")
    print("Hydrogen Isotopes:"+str(amount_HydrogenIsotopes))
    print("Nitrogen Isotopes:"+str(amount_NitrogenIsotopes))
    print("Oxygen Isotopes:"+str(amount_OxygenIsotopes))
    print("Hafnium:"+str(amount_Hafnium))
    print("Technetium:"+str(amount_Technetium))
    print("Caesium:"+str(amount_Caesium))
    print("Mercury:"+str(amount_Mercury))
    print("Platinum:"+str(amount_Platinum))
    print("Cadmium:"+str(amount_Cadmium))
    print("Vanadium:"+str(amount_Vanadium))
    print("Chromium:"+str(amount_Chromium))
    print("Cobalt:"+str(amount_Cobalt))
    print("Scandium:"+str(amount_Scandium))
    print("Silicates:"+str(amount_Silicates))
    print("Hydrocarbons:"+str(amount_Hydrocarbons))
    print("Promethium:"+str(amount_Promethium))
    print("Evaporite Deposits:"+str(amount_EvaporiteDeposits))
    print("Thulium:"+str(amount_Thulium))
    print("Dysprosium:"+str(amount_Dysprosium))
    print("Neodymium:"+str(amount_Neodymium))
    print("Titanium:"+str(amount_Titanium))
    print("Tungsten:"+str(amount_Tungsten))
    print("Atmospheric Gases:"+str(amount_AtmosphericGases))
    print("Megacyte:"+str(amount_Megacyte))
    print("Morphite:"+str(amount_Morphite))
    print("Pyerite:"+str(amount_Pyerite))
    print("Mexallon:"+str(amount_Mexallon))
    print("Isogen:"+str(amount_Isogen))
    print("Nocxium:"+str(amount_Nocxium))
    print("Zydrine:"+str(amount_Zydrine))
    print("Tritanium:"+str(amount_Tritanium))
    print("Heavy Water:"+str(amount_HeavyWater))
    print("Liquid OZone:"+str(amount_LiquidOzone))
    print("Strontium Calthrates:"+str(amount_StrontiumClathrates))
    print("Helium Isotopes:"+str(amount_HeliumIsotopes))
    print("======================")


    # calculate total amount in the ore

    total_HydrogenIsotopes = amount_HydrogenIsotopes * amount
    total_NitrogenIsotopes = amount_NitrogenIsotopes * amount
    total_OxygenIsotopes = amount_OxygenIsotopes * amount
    total_Hafnium =  amount_Hafnium * amount
    total_Technetium = amount_Technetium * amount
    total_Caesium =  amount_Caesium * amount
    total_Mercury = amount_Mercury * amount
    total_Platinum = amount_Platinum * amount
    total_Cadmium = amount_Cadmium * amount
    total_Vanadium = amount_Vanadium * amount
    total_Chromium = amount_Chromium * amount
    total_Cobalt = amount_Cobalt * amount
    total_Scandium = amount_Scandium * amount
    total_Silicates = amount_Silicates * amount
    total_Hydrocarbons = amount_Hydrocarbons * amount
    total_Promethium = amount_Promethium * amount
    total_EvaporiteDeposits = amount_EvaporiteDeposits * amount
    total_Thulium = amount_Thulium * amount
    total_Dysprosium = amount_Dysprosium * amount
    total_Neodymium = amount_Neodymium * amount
    total_Titanium = amount_Titanium * amount
    total_Tungsten = amount_Tungsten * amount
    total_AtmosphericGases = amount_AtmosphericGases * amount
    total_Megacyte = amount_Megacyte * amount
    total_Morphite = amount_Morphite * amount
    total_Pyerite = amount_Pyerite * amount
    total_Mexallon = amount_Mexallon * amount
    total_Isogen = amount_Isogen * amount
    total_Nocxium = amount_Nocxium * amount
    total_Zydrine = amount_Zydrine * amount
    total_Tritanium = amount_Tritanium * amount
    total_HeavyWater = amount_HeavyWater * amount
    total_LiquidOZone = amount_LiquidOzone * amount
    total_StrontiumCalthrates = amount_StrontiumClathrates * amount
    total_HeliumIsotopes = amount_HeliumIsotopes * amount

    print("TOTAL AMOUNTS in ORE")
    print("Hydrogen Isotopes:" + str(total_HydrogenIsotopes))
    print("Nitrogen Isotopes:" + str(total_NitrogenIsotopes))
    print("Oxygen Isotopes:" + str(total_OxygenIsotopes))
    print("Hafnium:" + str(total_Hafnium))
    print("Technetium:" + str(total_Technetium))
    print("Caesium:" + str(total_Caesium))
    print("Mercury:" + str(total_Mercury))
    print("Platinum:" + str(total_Platinum))
    print("Cadmium:" + str(total_Cadmium))
    print("Vanadium:" + str(total_Vanadium))
    print("Chromium:" + str(total_Chromium))
    print("Cobalt:" + str(total_Cobalt))
    print("Scandium:" + str(total_Scandium))
    print("Silicates:" + str(total_Silicates))
    print("Hydrocarbons:" + str(total_Hydrocarbons))
    print("Promethium:" + str(total_Promethium))
    print("Evaporite Deposits:" + str(total_EvaporiteDeposits))
    print("Thulium:" + str(total_Thulium))
    print("Dysprosium:" + str(total_Dysprosium))
    print("Neodymium:" + str(total_Neodymium))
    print("Titanium:" + str(total_Titanium))
    print("Tungsten:" + str(total_Tungsten))
    print("Atmospheric Gases:" + str(total_AtmosphericGases))
    print("Megacyte:" + str(total_Megacyte))
    print("Morphite:" + str(total_Morphite))
    print("Pyerite:" + str(total_Pyerite))
    print("Mexallon:" + str(total_Mexallon))
    print("Isogen:" + str(total_Isogen))
    print("Nocxium:" + str(total_Nocxium))
    print("Zydrine:" + str(total_Zydrine))
    print("Tritanium:" + str(total_Tritanium))
    print("Heavy Water:" + str(total_HeavyWater))
    print("Liquid OZone:" + str(total_LiquidOZone))
    print("Strontium Calthrates:" + str(total_StrontiumCalthrates))
    print("Helium Isotopes:" + str(total_HeliumIsotopes))
    print("======================")




    if total_HydrogenIsotopes > 0:
        value_of_HydrogenIsotopes = get_min_prices("Hydrogen Isotopes") * total_HydrogenIsotopes * base_reprocess_rate
    else:
        value_of_HydrogenIsotopes = 0

    if total_NitrogenIsotopes > 0:
        value_of_NitrogenIsotopes = get_min_prices("Nitrogen Isotopes") * total_NitrogenIsotopes * base_reprocess_rate
    else:
        value_of_NitrogenIsotopes = 0

    if total_OxygenIsotopes > 0:
        value_of_OxygenIsotopes = get_min_prices("Oxygen Isotopes") * total_OxygenIsotopes * base_reprocess_rate
    else:
        value_of_OxygenIsotopes = 0

    if total_Hafnium > 0:
        value_of_Hafnium = get_min_prices("Hafnium") * total_Hafnium * base_reprocess_rate
    else:
        value_of_Hafnium = 0

    if total_Technetium > 0:
        value_of_Technetium = get_min_prices("Technetium") * total_Technetium * base_reprocess_rate
    else:
        value_of_Technetium = 0


    if total_Caesium > 0:
        value_of_Caesium = get_min_prices("Caesium") * total_Caesium * base_reprocess_rate
    else:
        value_of_Caesium = 0

    if total_Mercury > 0:
        value_of_Mercury = get_min_prices("Mercury") * total_Mercury * base_reprocess_rate
    else:
        value_of_Mercury = 0

    if total_Platinum > 0:
        value_of_Platinum = get_min_prices("Platinum") * total_Platinum * base_reprocess_rate
    else:
        value_of_Platinum = 0

    if total_Cadmium > 0:
        value_of_Cadmium = get_min_prices("Cadmium") * total_Cadmium * base_reprocess_rate
    else:
        value_of_Cadmium = 0

    if total_Vanadium > 0:
        value_of_Vanadium = get_min_prices("Vanadium") * total_Vanadium * base_reprocess_rate
    else:
        value_of_Vanadium = 0

    if total_Chromium > 0:
        value_of_Chromium = get_min_prices("Chromium") * total_Chromium * base_reprocess_rate
    else:
        value_of_Chromium = 0

    if total_Cobalt > 0:
        value_of_Cobalt = get_min_prices("Cobalt") * total_Cobalt * base_reprocess_rate
    else:
        value_of_Cobalt = 0

    if total_Scandium > 0:
        value_of_Scandium = get_min_prices("Scandium") * total_Scandium * base_reprocess_rate
    else:
        value_of_Scandium = 0

    if total_Silicates > 0:
        value_of_Silicates = get_min_prices("Silicates") * total_Silicates * base_reprocess_rate
    else:
        value_of_Silicates = 0

    if total_Hydrocarbons > 0:
        value_of_Hydrocarbons = get_min_prices("Hydrocarbons") * total_Hydrocarbons * base_reprocess_rate
    else:
        value_of_Hydrocarbons = 0

    if total_Promethium > 0:
        value_of_Promethium = get_min_prices("Promethium") * total_Promethium * base_reprocess_rate
    else:
        value_of_Promethium = 0


    if total_EvaporiteDeposits > 0:
        value_of_EvaporiteDeposits = get_min_prices("Evaporite Deposits") * total_EvaporiteDeposits * base_reprocess_rate
    else:
        value_of_EvaporiteDeposits = 0

    if total_Thulium > 0:
        value_of_Thulium = get_min_prices("Thulium") * total_Thulium * base_reprocess_rate
    else:
        value_of_Thulium = 0

    if total_Dysprosium > 0:
        value_of_Dysprosium = get_min_prices("Dysprosium") * total_Dysprosium * base_reprocess_rate
    else:
        value_of_Dysprosium = 0

    if total_Neodymium > 0:
        value_of_Neodymium = get_min_prices("Neodymium") * total_Neodymium * base_reprocess_rate
    else:
        value_of_Neodymium = 0

    if total_Tritanium > 0:
        value_of_Titanium = get_min_prices("Titanium") * total_Titanium * base_reprocess_rate
    else:
        value_of_Titanium = 0

    if total_Tungsten > 0:
        value_of_Tungsten = get_min_prices("Tungsten") * total_Tungsten * base_reprocess_rate
    else:
        value_of_Tungsten = 0

    if total_AtmosphericGases > 0:
        value_of_AtmosphericGases = get_min_prices("Atmospheric Gases") * total_AtmosphericGases * base_reprocess_rate
    else:
        value_of_AtmosphericGases = 0

    if total_Megacyte > 0:
        value_of_Megacyte = get_min_prices("Megacyte") * total_Megacyte * base_reprocess_rate
    else:
        value_of_Megacyte = 0

    if total_Morphite > 0:
        value_of_Morphite = get_min_prices("Morphite") * total_Morphite * base_reprocess_rate
    else:
        value_of_Morphite = 0

    if total_Pyerite > 0:
        value_of_Pyerite = get_min_prices("Pyerite") * total_Pyerite * base_reprocess_rate
    else:
        value_of_Pyerite = 0

    if total_Mexallon > 0:
        value_of_Mexallon = get_min_prices("Mexallon") * total_Mexallon * base_reprocess_rate
    else:
        value_of_Mexallon = 0

    if total_Isogen > 0:
        value_of_Isogen = get_min_prices("Isogen") * total_Isogen * base_reprocess_rate
    else:
        value_of_Isogen = 0

    if total_Nocxium > 0:
        value_of_Nocxium = get_min_prices("Nocxium") * total_Nocxium * base_reprocess_rate
    else:
        value_of_Nocxium = 0

    if total_Zydrine > 0:
        value_of_Zydrine = get_min_prices("Zydrine") * total_Zydrine * base_reprocess_rate
    else:
        value_of_Zydrine = 0

    if total_Tritanium > 0:
        value_of_Tritanium = get_min_prices("Tritanium") * total_Tritanium * base_reprocess_rate
    else:
        value_of_Tritanium = 0

    if total_HeavyWater > 0:
        value_of_HeavyWater = get_min_prices("Heavy Water") * total_HeavyWater * base_reprocess_rate
    else:
        value_of_HeavyWater = 0

    if total_LiquidOZone > 0:
        value_of_LiquidOZone = get_min_prices("Liquid Ozone") * total_LiquidOZone * base_reprocess_rate
    else:
        value_of_LiquidOZone = 0

    if total_StrontiumCalthrates > 0:
        value_of_StrontiumCalthrates = get_min_prices("Strontium Clathrates") * total_StrontiumCalthrates * base_reprocess_rate
    else:
        value_of_StrontiumCalthrates = 0

    if total_HeliumIsotopes > 0:
        value_of_HeliumIsotopes = get_min_prices("Helium Isotopes") * total_HeliumIsotopes * base_reprocess_rate
    else:
        value_of_HeliumIsotopes = 0


    total_isk_value = 0
#    print(total_isk_value)
    total_isk_value = total_isk_value + value_of_HydrogenIsotopes
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_StrontiumCalthrates
#    print("StrontiumCalthrates:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_LiquidOZone
#    print("LiquidOZone:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_HeavyWater
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Tritanium
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Zydrine
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Nocxium
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Isogen
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Mexallon
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Pyerite
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Morphite
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Megacyte
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_AtmosphericGases
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Tungsten
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Titanium
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Neodymium
 #   print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Dysprosium
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Thulium
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_EvaporiteDeposits
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Promethium
 #   print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Hydrocarbons
#    print("Hydrogen:"+str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Silicates
#    print("Hydrogen:" + str(total_isk_value))
    total_isk_value = total_isk_value + value_of_Scandium
#    print(total_isk_value)
    total_isk_value = total_isk_value + value_of_Cobalt
#    print(total_isk_value)
    total_isk_value = total_isk_value + value_of_Chromium
 #   print(total_isk_value)
    total_isk_value = total_isk_value + value_of_Vanadium
#    print(total_isk_value)
    total_isk_value = total_isk_value + value_of_Cadmium
#    print(total_isk_value)
    total_isk_value = total_isk_value + value_of_Platinum
#    print(total_isk_value)
    total_isk_value = total_isk_value + value_of_Mercury
#    print(total_isk_value)
    total_isk_value = total_isk_value + value_of_Caesium
#    print(total_isk_value)
    total_isk_value = total_isk_value + value_of_Technetium
 #   print(total_isk_value)
    total_isk_value = total_isk_value + value_of_Hafnium
#    print(total_isk_value)
    total_isk_value = total_isk_value + value_of_OxygenIsotopes
#    print(total_isk_value)
    total_isk_value = total_isk_value + value_of_NitrogenIsotopes
#    print(total_isk_value)
    total_isk_value = total_isk_value + value_of_HeliumIsotopes

    print("Total ISK Value @ Jita Min Price of:"+str(amount)+" X "+ore+" is "+str(total_isk_value/100))
    print("Total ISK Value @ BuyBack Price of:" + str(amount) + " X " + ore + " is " + str(total_isk_value * 0.95 / 100))
    reprocessing_fee = (total_isk_value / 100 - (total_isk_value * 0.95 / 100))/2
    # print("% of Processing Fee Deducted:" + str((total_isk_value / 100 - (total_isk_value * 0.95 / 100))/2))
    print("% of Processing Fee Deducted:" + str(reprocessing_fee))
    total_after_fees = (total_isk_value * 0.95 / 100) - reprocessing_fee
    print("Contract Your Ore for:"+str(total_after_fees) )


def main():
    database = r"C:\Users\ed311\PycharmProjects\BuyBack\db.sqlite3"
    print("starting")
    # create a database connection
    conn = create_connection(database)
    with conn:
        get_value_from_ore(conn,"Compressed Veldspar","Tritanium")
        get_all_minerals_in_ore(conn, "Pristine Jaspet", 1996)
#        select_all_minerals(conn)
#        col_names_list = col_names(conn)
#        print(col_names_list)

main()