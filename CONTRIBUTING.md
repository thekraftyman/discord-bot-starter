# Contributing.md
Pull requests are welcome. Any and all pull requests need to go to the `dev` branch for testing before they can be merged into master.

##  Contribution Process
The most important rule is thus... __DON'T COMMIT TO MASTER BRANCH__.

With that in mind, small bug fixes and additions can be added to the `dev` branch. If
you plan on adding a ton of stuff that might take a while, I'd recommend creating a __new branch off of dev, not master__ (like what was done for version 2.0.0).

After a new addition has been tested in dev, then a pull request can be initiated to `master` to bring the bot up to the new code. So the process looks like this:
```
(new branch) --> dev --> master
```

## Version Number

Along with new changes, make sure that `Version` is updated to the new version number. In short, the version goes:
> major_version.minor_version.patch

For example, when bug fixes were made to `1.2.0`, the version updated to `1.2.1`. When new functionality was added to the code after `1.1.0`, the version updated to `1.2.0`. When the bot's architecture was updated to a better standard (completely changing the programming process), the version went to `2.0.0`.

## Changelog updates

All contributions should be accompanied by a new entry in the `CHANGELOG.md` file. Within that file there are instructions on how to update it.
