# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/robot.svg" card_color="#22A7F0" width="50" height="50" style="vertical-align:bottom"/> Grocy
Interacts with your private [grocy instance](https://grocy.info/)

## About
This [mycroft](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft) skill enables you to "talk" with [grocy](https://grocy.info).
It requires a running self-hosted instance of [grocy](https://grocy.info)
([Installation](https://github.com/grocy/grocy#how-to-install)).

Currently, the skill has only a limited set of features:
### Examples
* "Put milk on the shopping list"
* "How much bread do we have at home"
* "Remind me what I want to buy"

For "mass" insertion of bought products:
- "I was shopping"  (Mycroft: "What did you buy?")
- "1 Cucumber"
- "1 Milk"
- ...
- "That was all"
- Note: this uses always the default purchase quantity unit

## Known Limitations

Sometimes there are problems to match right product in grocy.
Example: you say: "How many egg***s*** do we have at home?"
If the product in grocy is named "egg", then it isn't found.

## Configuration

To use this skill, you must configure at least the hostname.
Depending on your setup, you may also need to configure:
- the port number of grocy (default 80)
- an api-key (default "")
- http or https? (default "http")
- base path (default "/")

Port number, protocol and hostname can be configured by saying
"Configure grocy" to mycroft, which starts a configuration dialog.
If you [paired your device](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/pairing-your-device), 
the other settings can be configured at [account.mycroft.ai/skills](https://account.mycroft.ai/skills).
Otherwise they can be set in the file "~/.config/mycroft/grocy-skill/settings.json".

## Languages
* English
* German

## Credits
fipwmaqzufheoxq92ebc

## Category
**Daily**
Productivity
Information

## Tags

