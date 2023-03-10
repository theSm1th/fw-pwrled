# fw-pwrled

This is a small program to change the colour of the Framework Laptop's power button LED depending on the battery state.

By default, this program will check every 15 seconds if the battery is below 20%, where the power LED will change to red - alternatively, if the battery is charging, it will become green.

Included in the repo is the program and a template systemd unit file for executing the program on startup - you will have to change the path included to where you cloned the repo locally.

## Dependency (singular)
You'll need a copy of DHowett's excellent fw-ectool in your PATH for this to work correctly. Build instructions can be found [here](https://www.howett.net/posts/2021-12-framework-ec/#using-fw-ectool).



I made this because I was bored. If you have any suggestions or issues, please open a github issue.
