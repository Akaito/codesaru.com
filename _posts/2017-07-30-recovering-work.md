---
date:       2017-07-30 09:41 -07:00
title:      Recovering work
categories: noise
slug:       recovering-work
---

Recovering my old starting point made during recovery from surgery.

During eleven bed-ridden days, restarted an even older project to make a platformer with fun movement.
There are two primary inspirations for the work:
1. Implementing the old N Ninja math tutorials for how their collision works.
    - [Tutorial A](http://www.metanetsoftware.com/technique/tutorialA.html)
    - [Tutorial B](http://www.metanetsoftware.com/technique/tutorialB.html)
2. Supporting every sample from the ActionGame Algorithm Maniax book.
    - Japanese programming book that reverse-engineers action game characters/mechanics from the 80s up.

<!-- TODO: Add links to the above -->

<!-- more -->

The first goal is to use N Ninja-esque collision, and support every or almost every character/mechanic explained in the ActionGame book.

The work is all being done on Linux first.
Windows support will eventually happen.
Working completely within Linux is what I'm doing right now.
So all tools used must also work there.

Main tools so far are:
- [clang](http://clang.llvm.org/) for C++.
- [Vim](http://www.vim.org/) for code/text file editing.
- [Terminator](https://wiki.archlinux.org/index.php/Terminator) for terminal multiplexing.
- [gdb](https://sourceware.org/gdb/) for debugging.

No code tags, intellisense, or anything like that yet.
I'll get around to it eventually, when the code's complex enough to warrant it.

# 1. Projection test

<img src="{{ "/assets/images/" | relative_url }}2017-07-30_projection.gif"/>

Just get a vector p1-&gt;p0 (red-&gt;blue) projected onto the line segment p1->p2 (red->green).
Make the handles draggable for testing.

- [SDL2](https://www.libsdl.org/) for window and input management, and rendering.  Also their wonderful assert/trap/continue.
- [OpenGL 2](https://www.opengl.org/) for some other rendering.
- [Dear ImGui](https://github.com/ocornut/imgui) for an easy way to both debug and poke things.
    I liked AntTweakBar in the past, but wanted something a little more modern in its API, and I liked that Dear ImGui *doesn't* make its own draw calls.
- [CML](http://cmldev.net/) (Configurable Math Library) for vectors, points, etc.

# 2. SAT box test

<img src="{{ "/assets/images/" | relative_url }}2017-07-30_sat-box.gif"/>

Mimic the Metanet tutorial sample seen [here](http://www.metanetsoftware.com/technique/tutorialA.html#section1) (Flash required).
Shows what the projection of the box in the middle looks like on the line.
Line can be moved around the box with the handle.
Don't mind the floating "p0" text.
That's an ImGui tooltip, which displays at the cursor's position.

# 3. SAT boxes test

<img src="{{ "/assets/images/" | relative_url }}2017-07-30_sat-boxes.gif"/>

Have two moveable rectangular objects.
If they overlap, show a vector that is the smallest movement of the red box available to separate the boxes.

# 4. SAT triangle test

<img src="{{ "/assets/images/" | relative_url }}2017-07-30_sat-tri.gif"/>

Change one of the shapes to a triangle.
Two legs must be axis-aligned.
Press 'R' to resolve the "collision" by moving the red box out of the triangle the shortest possible distance.

# 5. SAT convex test

<img src="{{ "/assets/images/" | relative_url }}2017-07-30_sat-convex.gif"/>

SAT test supports any two arbitrary convex shapes.

# 6. tile test

<img src="{{ "/assets/images/" | relative_url }}2017-07-30_tiles.gif"/>

Add a tile map/world.
Add a camera.

- Tile assets by Kenney; you can find them in the [voxel pack](http://kenney.nl/assets/voxel-pack).
- Tilemap files edited with [Tiled](http://www.mapeditor.org/).
- "Mod" support with Icculus' [PhysicsFS](https://www.icculus.org/physfs/).
- Texture/image loading with the single-header library [stb_image.h](https://github.com/nothings/stb).
- XML parsing with [TinyXML](http://www.grinninglizard.com/tinyxml2/index.html).

# 7. platformer test

<img src="{{ "/assets/images/" | relative_url }}2017-07-30_platformer-gravity-wrap.gif"/>
<img src="{{ "/assets/images/" | relative_url }}2017-07-30_platformer-triangle-anim.gif"/>

Red character is driven by "player 1" controls.
Other characters share "player 2" controls.
Controls are deliberately limited to four directions and one button.
May become two directions and two buttons.
Animations are hand-made XML for the time being.

Characters "wrap" by default if collision doesn't stop them.
Rendering updated so wrapping characters show on both sides of the screen (hacky).

Characters are controlled by Lua scripts.
Scripts choose whether to turn tile world collision on or off, and whether or not they want gravity handled for them automatically.
One of the goals is to make it very easy for a person with zero programming experience to make something fun.
But without taking away so much control that an advanced user couldn't do something completely unexpected.
Like every other file being loaded from disk, these can be "modded" (replaced or added to).

```lua
-- simplest-player.lua
m_x = 0

function move()
    if input.right then
        m_x = m_x + 20
    end
end
```

Tile collision (the second pass written) is built in the N Ninja style, from the Metanet tutorials.
The borders between "empty space" and "solid tile with a plain edge" can be shown in red.
No support for "interesting" edges yet (curves, cut-away tiles, etc.).

- Character assets by Kenney; you can find them in the [abstract platformer pack](http://www.kenney.nl/assets/abstract-platformer).
- Started using [Valgrind](http://valgrind.org/) to check for leaks.
    Found a couple of my own, but most leaks are specific to being on a Surface Pro 3's hardware/drivers.
    Thankfully Valgrind makes it easy to build up an "ignore" file, too.

