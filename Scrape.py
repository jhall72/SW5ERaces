from selenium import webdriver
import time

parsed = []
with open("T:\StarWarsOutput.txt", "a", encoding="utf-8") as file_object:
    with open('T:\Parse.txt') as fp:
        for line in fp:
            x = line.split(">")
            if x[0] not in parsed:
                file_object.write("\n")
                file_object.write(x[0])
                print("PARSING: " + x[0])
                file_object.write("\n")
                #try:
                options = webdriver.ChromeOptions()
                options.add_argument("--enable-javascript")
                driver = webdriver.Chrome(executable_path=r'C:\Users\John\Downloads\chromedriver_win32\chromedriver.exe', options=options);
                driver.get(x[0])
                time.sleep(60)
                htmlSource = driver.page_source
                file_object.write(htmlSource)
                driver.quit()
                parsed.append(x[0])
                #except:
                    #file_object.write("ISSUE WITH: " + x[0])
                    #print("ISSUE WITH: " + x[0])
            else:
                print("SKIPPING: " + x[0] + " AS IT HAS ALREADY BEEN PARSED.")