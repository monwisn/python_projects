# SIMPLE DISCORD BOT - PYTHON

To create a Discord bot using Python, follow these steps:

1. Create Discord User Account or log in to an existing account.


2. Create Your Discord Server by clicking the plus icon on the left side. 


3. Create Your Python Project and Add the Virtual Environment.


4. Set up a new Discord application:
   - Go to the Discord Developer Portal (https://discord.com/developers/applications),
   - Click on "New Application" and give it a name,
   - Navigate to the "Bot" tab and customize your bot's settings if desired (Username, Icon). Remember to Save Changes,
   - Click on "Message Content Intent" in the same tab (Required for bot to receive message content.) and Save Changes.


5. Get the bot token:
   - Go to "Bot" tab, click 'Reset Token', click "Copy" to copy the generated token,
   - Keep this token secure, as it will be used to authenticate your bot. (Save Token in your .env project file)


6. Generate Bot Scopes and permissions:
   - Go to "OAuth2" tab and click "URL Generator",
   - Select "bot" in Scopes section,
   - Next, select permissions that bot will be allowed to access 
   - Our bot permissions:
     ("Manage Server", "Read Messages/View Channels", "Send Messages", "Manage Messages", "Read Message History")
   - Click "Copy" below the permissions (GENERATED URL),
   - Go to your searchbar and paste the copied url,
   - Now you can invite your bot your server -> Select your Server and click "Continue",
   - All the selected permissions will be there, click "Authorize" button,
   - Now bot has been authorized and added to your server.
   


7. Install the necessary libraries:
   - Open your terminal or command prompt.
   - Run `pip install discord.py` to install the discord library.
   - Run `pip install python-dotenv` to install the environment library.


8. Write the bot code:
   - Create a new Python file, import necessary libraries,
   - Create a new instance of the `discord.Client` class: `client = Client()` and add intents,
   - Implement event handlers to handle bot events (e.g., `on_ready`, `on_message`, `send_message`).


9. Implement the bot functionality:
   - Within the event handlers, write the code to perform actions based on specific events (e.g., sending messages),


10. Run the bot:
   - In your terminal or command prompt, navigate to the directory where your bot code is located.
   - Run the Python file: `python your_bot_file.py` or click "run" in `if __name__ == '__main__`
   - If everything is set up correctly, you should see your bot come online in your Discord server.
