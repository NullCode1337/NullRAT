![NullRAT](https://user-images.githubusercontent.com/70959549/150108231-0c8a8b30-a3cf-4a94-8712-2277cd833731.png)

<h1 align=left>Getting Variables</h1>
<h4 align=left><b>How (and why) to get all the required variables necessary for the usage of NullRAT:</b></h4>
<h1>Table of Contents:</h2>

1. [Proper Bot Invite](https://github.com/NullCode1337/NullRAT/edit/source/Getting%20Variables.md#proper-bot-invite-link)
2. [Discord Bot Token](https://github.com/NullCode1337/NullRAT/blob/source/Getting%20Variables.md#discord-bot-token)
3. [Channel ID](https://github.com/NullCode1337/NullRAT/blob/source/Getting%20Variables.md#channel-id)
4. [Server ID(s)](https://github.com/NullCode1337/NullRAT/blob/source/Getting%20Variables.md#server-ids)

---
<h3>Proper Bot Invite Link</h3>

Many people have been generating invalid invites, and when NullRAT doesn't work as expected, they blame me.</br></br>
**Here's how to do it:**

1. Open [https://discord.com/developers/applications](https://discord.com/developers/applications) in a browser window.

![Discord Developer Portal](https://user-images.githubusercontent.com/70959549/150104339-5b6edaf2-26ec-4438-9d08-cd82473db39e.png)

2. If you already have an application, click on it. Otherwise, make one.

![Applications side menu](https://user-images.githubusercontent.com/70959549/162367526-4432adea-0998-45b8-a151-958d86c331be.png)

3. Click on `OAuth2`, then `URL Generator`

![Scopes](https://user-images.githubusercontent.com/70959549/162367784-5f53d2aa-00c8-419f-b5bc-80058437ad66.png)

5. Important! Select the scopes `bot` **and** `application.commands`. Without these 2 NullRAT will never work as expected
6. Now select any permission you want (I go for Administrator only), then copy the invite link. Done

---
<h3>Discord Bot Token</h3>

This is used to run NullRAT's core bot host. **Without this NullRAT will straight up crash**

**How to obtain it:**

1. Open [https://discord.com/developers/applications](https://discord.com/developers/applications) in a browser window.

![Discord Developer Portal](https://user-images.githubusercontent.com/70959549/150104339-5b6edaf2-26ec-4438-9d08-cd82473db39e.png)

2. If you already have an application, click on it. Otherwise, make one.
3. Once you see the applications window, press Bot.

![Bot menu](https://user-images.githubusercontent.com/70959549/162366786-79152640-19fe-4f7b-92d4-4aafebbfc85d.png)

5. Click on `Reset Token` so that the gods at Discord allow us to view the token

![Bot menu](https://user-images.githubusercontent.com/70959549/162367155-348a6408-2b77-402a-83b0-f13b311d3288.png)

7. Click on `Copy` and store it somewhere. Done!

---
<h3>Channel ID</h3>

This is required for NullRAT to send alerts in the specified channel. **Without this NullRAT will be unable to send notifications**

**How to obtain it:**

1. Open your Discord client/web.
2. Goto account settings.
3. There, click on `Advanced` and enable `Developer Mode`.

![image](https://user-images.githubusercontent.com/70959549/150111475-d1cd44c1-98e2-4dd6-be07-90b87df7f624.png)

4. Now go back to your discord server, and right click on the channel you want to send notifications.

![image](https://user-images.githubusercontent.com/70959549/150112161-5ba2ac87-7311-4fa7-96ee-717ec369bfb9.png)

5. Click on `Copy ID` and store it somewhere. Done!

---
<h3>Server ID(s)</h3>

This is required for NullRAT to set the command handler. **Without this you won't be able to send any commands to NullRAT**

**How to obtain it:**

1. Enable Developer Mode. If not already enabled:
   - Open your Discord client/web.
   - Goto account settings.
   - There, click on `Advanced` and enable `Developer Mode`.

2. Now, go back to your discord server.
3. Right click on the server icon, and click on `Copy ID`. Done! (Don't forget to store it)

![image](https://user-images.githubusercontent.com/70959549/150113522-fa9b8cf7-d3bc-4b8d-b448-e6c515f546f4.png)

---

<p align=right><b>Guide written by NullCode</b></p>
