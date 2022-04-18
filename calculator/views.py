from django.shortcuts import render
from .forms import Inventory
from functools import wraps
from urllib.request import Request
from re import sub
from bs4 import BeautifulSoup
import re
import requests
import lookup


value = 0

def split_and_strip(s):
    """
    Strip each line and split by new line. Also, removes empty lines
    :param str string: String to be split and stripped
    """
    # Strip each line
    lines = [line.strip(' ').replace(u"\xa0", u"").replace(u"\xc2", u"")
             for line in s.strip(' ').replace("\r\n", "\n").split('\n')]
    # Return non-empty lines
    return [line for line in lines if line]


def regex_match_lines(regex, lines):
    """
    Performs a regex search on each line and returns a list of matched groups
    and a list of lines which didn't match.
    :param regex regex: String to be split and stripped
    :param list lines: A list of strings to perform the regex on.
    """
    matches = []
    bad_lines = []
    for line in lines:
        match = regex.search(line)
        if match:
            matches.append(match.groups())
        else:
            bad_lines.append(line)
    return matches, bad_lines


def f_int(num):
    """ Converts a given numeric string into an integer
    :param string num: A string of the format "123,456", "123'456", "123 456"
                    or "123456"
    """
    if num is None:
        return
    try:
        return int(sub(r"[,'\. ']", '', num))

    except ValueError:
        return 0


def unpack_string(funct):
    """ This allows parsers to be passed a single string instead of a list of
        strings. The raw parsers take in a list of strings. This is to enable
        the ability to parse input that is of multiple types by chaining
        bad_lines into multiple parsers.
    """
    @wraps(funct)
    def wrapper(paste_string):
        return funct(split_and_strip(paste_string))

    return wrapper


def get_prices(itemid):
        url = "https://api.evemarketer.com/ec/marketstat?usesystem=30000142&typeid="+str(itemid)
        headers = {'User-Agent': 'Mozilla/5.0'}
        request = Request(url, headers=headers)
        response = requests.get(url).text
        xmldoc = response
        content = BeautifulSoup(xmldoc,features='html.parser')
        avg = content.find_all("avg")
        value_str = avg[1]
        value2 = str(value_str).replace('<avg>', '')
        value = str(value2).replace('</avg>', '')
        return value


def get_min_prices(min):
    list_of_minerals = [
                      "34","Tritanium",
                      "35","Pyerite",
                      "36","Mexallon",
                      "37","Isogen",
                      "38","Nocxium",
                      "39","Zydrine",
                      "40","Megacyte",
                      "11399","Morphite",
                      "16272","Heavy Water",
                      "16273","Liquid Ozone",
                      "16274","Helium Isotopes",
                      "17887","Oxygen Isotopes",
                      "17888","Nitrogen Isotopes",
                      "17889","Hydrogen Isotopes",
                      "16275","Strontium Clathrates",
                      "16633","Hydrocarbons",
                      "16634","Atmospheric Gases",
                      "16635","Evaporite Deposits",
                      "16636","Silicates",
                      "16637","Tungsten",
                      "16638","Titanium",
                      "16639","Scandium",
                      "16640","Cobalt",
                      "16641","Chromium",
                      "16642","Vanadium",
                      "16643","Cadmium",
                      "16644","Platinum",
                      "16646","Mercury",
                      "16647","Caesium",
                      "16648","Hafnium",
                      "16649","Technetium",
                      "16650","Dysprosium",
                      "16651","Neodymium",
                      "16652","Promethium",
                      "16653","Thulium",
                      "28694","Amber Mykoserocin",
                      "28695","Azure Mykoserocin",
                      "28696","Celadon Mykoserocin",
                      "28697","Golden Mykoserocin",
                      "28698","Lime Mykoserocin",
                      "28699","Malachite Mykoserocin",
                      "28700","Vermillion Mykoserocin",
                      "28701","Viridian Mykoserocin",
                      "25268","Amber Cytoserocin",
                      "25279","Azure Cytoserocin",
                      "25275","Celadon Cytoserocin",
                      "25277","Lime Cytoserocin",
                      "25276","Malachite Cytoserocin",
                      "25278","Vermillion Cytoserocin",
                      "25274","Viridian Cytoserocin",
                      "30375","Fullerite-C28",
                      "30376","Fullerite-C32",
                      "30377","Fullerite-C320",
                      "30370","Fullerite-C50",
                      "30378","Fullerite-C540",
                      "30371","Fullerite-C60",
                      "30372","Fullerite-C70",
                      "30373","Fullerite-C72",
                      "30374","Fullerite-C84"
                       ]
    item = list_of_minerals.index(min)
    price = get_prices(list_of_minerals[item-1])
    print(min+":"+str(price))
    return price


def calculator(request):

    context={}
    context['form'] = Inventory
    context['value'] = value

    if request.method == "POST":
        pasted_form = Inventory(request.POST)
        if pasted_form.is_valid():
            context['posted'] = "TRUE"
            assets = request.POST.getlist('paste_inventory')
            list = assets[0]
            list_string = "".join(str(x) for x in list)
            clean_list = list_string.strip("\t")
            res = re.split('(\d+)', str(clean_list))
            i = 0
            clean_asset_list = []
            while(i < len(res)-1):
                clean_asset_list.append(res[i].strip())
                clean_asset_list.append(res[i+1])
                i += 2
            context['items_found'] = clean_asset_list
            return render(request, 'calculator/calculator.html', context)
    return render(request, 'calculator/calculator.html', context)
