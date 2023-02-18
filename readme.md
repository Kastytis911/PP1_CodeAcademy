Practical project 1. Code academy

In this project we need to create scraper program.

For launch program:
    1. Open "app.py";
    2. In line 20, is program call "Selected_url = read_config.read_url(0)". 
    In "...read_url(0)" we need to chose 0 (if we want to get men jackets with prices from "Audimas" shop),
    or 1 (if we want to get woman jackets with prices from "Audimas" shop)
    3.Run program.

In "logs" folder ar "main.log" file. This file is saving some errors, if program willl crash.

Program working:
    1. When we run "app.py" file, first we get url, from config.txt file, depend what number we choose;
    2. Next program scrape "Audimas" online shop, and return jackets type, and price;
    3. In python console print jackets type and price;
    4. All this information, send to local "MySql" database

