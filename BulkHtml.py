import streamlit as st
import zipfile
import os

# Function to create an HTML file
def create_html_file(city_name, html_content):
    file_name = f"Gold-rate-{city_name.lower().replace(' ', '-')}.html"
    with open(file_name, "w") as file:
        file.write(html_content)
    return file_name

# Function to zip all HTML files
def zip_files(file_names):
    zip_file_name = "html_files.zip"
    with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
        for file_name in file_names:
            zip_file.write(file_name)
            os.remove(file_name)  # Remove the individual file after adding it to the zip
    return zip_file_name

# Streamlit App
st.title("Bulk HTML File Generator")

html_content = st.text_area("Enter the HTML content:")
city_names = st.text_area("Enter the city names (comma separated):")

if st.button("Generate HTML Files"):
    if html_content and city_names:
        city_list = [city.strip() for city in city_names.split(",")]
        generated_files = [create_html_file(city, html_content) for city in city_list]

        # Zip the generated files
        zip_file_name = zip_files(generated_files)
        
        # Provide a download link
        with open(zip_file_name, "rb") as zip_file:
            st.download_button(
                label="Download All HTML Files",
                data=zip_file,
                file_name=zip_file_name,
                mime="application/zip"
            )
