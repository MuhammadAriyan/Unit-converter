import streamlit as st
# Dictionary of unit with their units
unit = {
    "Length": {
        "meter": "m", "kilometer": "km", "centimeter": "cm", "millimeter": "mm", "micrometer": "µm", "nanometer": "nm", 
        "mile": "mi", "yard": "yd", "foot": "ft", "inch": "in", "nautical mile": "NM"
    },
    "Mass": {
        "kilogram": "kg", "gram": "g", "milligram": "mg", "microgram": "µg", "tonne": "t", "pound": "lb", "ounce": "oz", "stone": "st"
    },
    "Area": {
        "square meter": "m²", "square kilometer": "km²", "square centimeter": "cm²", "square millimeter": "mm²", 
        "square mile": "mi²", "square yard": "yd²", "square foot": "ft²", "square inch": "in²", "hectare": "ha", "acre": "ac"
    },
    "Temperature": {
        "Celsius": "°C", "Kelvin": "K", "Fahrenheit": "°F", "Rankine": "°R"
    },
    "Plane Angle": {
        "degree": "°", "radian": "rad", "gradian": "gon", "arcminute": "′", "arcsecond": "″"
    },
    "Digital Storage": {
        "bit": "b", "byte": "B", "kilobit": "kb", "kilobyte": "kB", "megabit": "Mb", "megabyte": "MB", 
        "gigabit": "Gb", "gigabyte": "GB", "terabit": "Tb", "terabyte": "TB", "petabyte": "PB"
    }
}

conversion = {
    "Length": { 
        ("meter", "kilometer"): lambda x: x * 0.001, ("kilometer", "meter"): lambda x: x * 1000,
        ("meter", "centimeter"): lambda x: x * 100, ("centimeter", "meter"): lambda x: x * 0.01,
        ("meter", "millimeter"): lambda x: x * 1000, ("millimeter", "meter"): lambda x: x * 0.001,
        ("kilometer", "mile"): lambda x: x * 0.621371, ("mile", "kilometer"): lambda x: x * 1.60934,
        ("yard", "meter"): lambda x: x * 0.9144, ("meter", "yard"): lambda x: x * 1.09361,
        ("foot", "meter"): lambda x: x * 0.3048, ("meter", "foot"): lambda x: x * 3.28084,
        ("inch", "centimeter"): lambda x: x * 2.54, ("centimeter", "inch"): lambda x: x * 0.393701
    },
    "Mass": { 
        ("kilogram", "gram"): lambda x: x * 1000, ("gram", "kilogram"): lambda x: x * 0.001,
        ("kilogram", "pound"): lambda x: x * 2.20462, ("pound", "kilogram"): lambda x: x / 2.20462,
        ("gram", "milligram"): lambda x: x * 1000, ("milligram", "gram"): lambda x: x * 0.001,
        ("pound", "ounce"): lambda x: x * 16, ("ounce", "pound"): lambda x: x * 0.0625
    },
    "Area": { 
        ("square meter", "square kilometer"): lambda x: x * 1e-6, ("square kilometer", "square meter"): lambda x: x * 1e6,
        ("square meter", "square foot"): lambda x: x * 10.7639, ("square foot", "square meter"): lambda x: x * 0.092903,
        ("square mile", "square kilometer"): lambda x: x * 2.58999, ("square kilometer", "square mile"): lambda x: x * 0.386102
    },
    "Temperature": {
        ("Celsius", "Kelvin"): lambda c: c + 273.15, ("Kelvin", "Celsius"): lambda k: k - 273.15,
        ("Celsius", "Fahrenheit"): lambda c: (c * 9/5) + 32, ("Fahrenheit", "Celsius"): lambda f: (f - 32) * 5/9,
        ("Fahrenheit", "Kelvin"): lambda f: (f - 32) * 5/9 + 273.15, ("Kelvin", "Fahrenheit"): lambda k: (k - 273.15) * 9/5 + 32
    },
    "Plane Angle": { 
        ("degree", "radian"): lambda x: x * 0.0174533, ("radian", "degree"): lambda x: x * 57.2958,
        ("degree", "gradian"): lambda x: x * 1.11111, ("gradian", "degree"): lambda x: x * 0.9
    },
    "Digital Storage": { 
        ("bit", "byte"): lambda x: x * 0.125, ("byte", "bit"): lambda x: x * 8,
        ("kilobyte", "byte"): lambda x: x * 1000, ("byte", "kilobyte"): lambda x: x * 0.001,
        ("megabyte", "kilobyte"): lambda x: x * 1000, ("kilobyte", "megabyte"): lambda x: x * 0.001,
        ("gigabyte", "megabyte"): lambda x: x * 1000, ("megabyte", "gigabyte"): lambda x: x * 0.001,
        ("terabyte", "gigabyte"): lambda x: x * 1000, ("gigabyte", "terabyte"): lambda x: x * 0.001
    }
}

def convert(category, from_unit, to_unit, value):
    if category not in conversion:
        return f"Category '{category}' not found"
    
    if from_unit == to_unit:
        return f"{value} {unit[category][from_unit]}"

    if (from_unit, to_unit) in conversion[category]:
        return conversion[category][(to_unit, from_unit)](value)

    if (to_unit, from_unit) in conversion[category]: 
        return 1 / (conversion[category][(to_unit, from_unit)](value))

    return f"No conversion available for {from_unit} to {to_unit}"



# page configuration

st.set_page_config(page_title="Unit Converter", page_icon="📏",layout='centered')

# title of the app
st.title("Distance Converter 🎍")
# category selection 
conversionFactorbyCategory = st.selectbox("Select the unit category 🥓", list(conversion.keys()))
# 2 cols for both unit
col1,col2 = st.columns(2)
with col1:
    # slect initial unit
    initialUnit = st.selectbox("Select the initial unit ✨", unit[conversionFactorbyCategory])
with col2:
    # select final unit
    finalUnit = st.selectbox("Select the final Unit 🎋", unit[conversionFactorbyCategory])

# input value
initialValue = st.number_input("Enter the initial value 🎑", value=0.0)
result = st.empty()
# convert button   
if st.button("Convert"):
    # convert the value
    result = convert(conversionFactorbyCategory, initialUnit, finalUnit, initialValue)
    # display the response
    st.subheader(result)
    st.balloons()
    st.toast('Conversion Successful! 🎉', icon="🎉")
st.snow()
