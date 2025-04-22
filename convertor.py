import streamlit as st

#1- unit converter application
#2- inout for unit converter appliction
#3- output given by unit application

# inputs
#1- value
#2- unit from conversion/ kis unit se convert krna h
#3- unit to conversion/ kis unit mn convert krna h

# value  unit_from  unit_to
# 2000    meters    kilomeaters

# output
# converted value in preffered unit type

#                  2.0/1.5
def convert_units(value: float, unit_form: str, unit_to: str ):
    # print("value>>>",value)
    # print("unit_from>>>",unit_form)
    # print("unit_to>>>",unit_to)
    
    if unit_form == "kliometers" and unit_to == "meters":
        return value * 1000
    elif unit_form == "meters" and unit_to == "kilometers":
        return value * 0.001
    elif unit_form == "kilograms" and unit_to == "grams":
        return value * 1000
    elif unit_form == "grams" and unit_to == "kilograms":
        return value * 0.001
    else:
        return "conversion is not supported"


# results and output ki value
# result1 = convert_units(1.5,"klimeters","meters")
# print("the result in meters is", result1)
# result2 = convert_units(5000,"grams","kilograms")
# print("the value in kilograms is", result2)


def main():
    st.title("Unit Converter")
    st.write("Welcom to unit converter!")

    value = st.number_input("Enter the value you want to convert:", min_value=0.0)
    unit_from = st.text_input("Enter the unit you want to convert from: (e.g. meters, kilometers, grams, kilograms)")
    unit_to = st.text_input("Enter the unit you want to conversion: (e.g. meters, kilometers, grams, kilograms)")
    
    if st.button("convert"):
        result = convert_units(value, unit_from,unit_to)
        st.write("converted value is :",result)

    # print("value>>>",value)
    # print("unit_to>>>",unit_to)
    # print("unit_form>>>",unit_form)
    # result = convert_units(value, unit_form,unit_to)
    # print(" converted value is :", result)

main()