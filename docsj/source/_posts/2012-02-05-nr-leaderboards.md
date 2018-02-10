---
layout:     post
title:      "Global and Friend Leaderboards Without Accounts"
date:       2012-02-05 00:00:00 -0700
categories: stories
slug:       nr-leaderboard
---
When making the online leaderboard for [Nitronic Rush](/projects/nitronic-rush), these were the considerations:

- **As easy as possible to implement.** Only 6 days remained before the game was to be released.
- **No user accounts.** It should be as close to the old arcade feeling as possible (just your initials). No registration process, and no password to memorize.
- **No cheat-prevention.** Any cheat-prevention written in only six days would be broken in about as few. And having it there turns cheating into a fun puzzle to figure out.
- **Let users play with just their friends.** Playing against a world-wide top-ten is only fun for a select few. Plus cheaters will show up in that list.
- **Auto-magically work with user-created levels.** Any new levels should work with the leaderboard, without any effort on the user's part.

Given these guidelines, one of the major differences in this leaderboard system from others I've seen arose. The "Friend Group" system was created so users could <em>avoid</em> cheaters, rather than preventing or punishing them.

Every user has a Friend Group. It's just an arbitrary string of reasonable length (a few words at most). The default Friend Group is "world" (case-insensitive). When a score is posted, its Friend Group is tracked. So the first level of Nitronic Rush has a leaderboard for "world", another for "china", and another for, say, "tom_and_me". Aside from "world", users created these by just typing in a different Friend Group; there's no pre-defined list.

Once a score is posted to a Friend Group, that Friend Group exists.

If playing with the "world" Friend Group, this can be considered to be the world-wide leaderboard that so many other games have. Technically, one group is no different from another. If you want to avoid cheaters that begin to appear on a Group, or you want to play with just a small group of friends, change your Friend Group. You see only other people with the same Friend Group, and you can change your Friend Group at any time. At time of writing, about half of the Nitronic Rush leaderboard entries are in the "world" Friend Group. Though players can easily post their scores to different Friend Groups, and move around between them at will.

With just one user-entered string, users can play together with friends and avoid cheaters. Completely anonymously and without accounts, friends lists, or passwords.

<br />

*After-thought:* Comparison with the [Wii friend code][]. Wii friend codes are good for pretty-secure, person-to-person friend interaction. Both parties need to know the other's lengthy, difficult-to-memorize, randomly-generated (per-game/system combo) string.  The "Friend Group" system in Nitronic Rush isn't as "secure" or "closed" a group as Wii friends, and so is not as suitable for games where very young children are a major part of the demographic. However, the Friend Group approach allows for some random encounters (such as if two people independently decide to use the "france" Friend Group). Plus, only one easy-to-remember and fairly short string is required for any number of people who wish to play together.

[Nitronic Rush]: /projects/nitronic-rush
[Wii friend code]: http://en.wikipedia.org/wiki/Friend_Code#Friend_Codes
