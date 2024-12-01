import streamlit as st
st.title('Items App made by Lisa')
name = st.text_input ("Please enter your name:")
flour_bag_cost = 2
num_flour_bags = 4 
egg_carton_cost = 3
num_egg_cartons = 2
chocolate_chip_pack_cost = 4
num_chocolate_chip_packs = 5
total_flour = flour_bag_cost*num_flour_bags
total_eggs = egg_carton_cost*num_egg_cartons 
total_chocolate = chocolate_chip_pack_cost*num_chocolate_chip_packs
total_items = total_flour + total_eggs + total_chocolate 
("Hi",name, "After using your discount", "you spent a total of $",total_items," on your baking supplies.")