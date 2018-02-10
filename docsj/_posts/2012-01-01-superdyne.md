---
layout:     post
title:      "Superdyne Common Architecture"
date:       2011-08-01 01:01:01 -0700
date_begin: 2010
date_end:   2012
categories: projects
slug:       superdyne
images:     SuperdyneGraphViz.png
---
<div class="post_pictures">
  <div class="post_pictures_main">
    <a href="{{ "/assets/images/SuperdyneGraphViz.png" }}">
      <img src="{{ "/assets/images/thumbs/SuperdyneGraphViz.png" }}"/>
      <!-- <img src="{{ "/assets/images/thumbs/SuperdyneGraphViz.png" | absolute_url }}"/> -->
    </a>
  </div> <!-- post_pictures_main -->
</div> <!-- /post_pictures -->

As part of working on [Nitronic Rush][], I worked with another technical director/architect (<a href="http://www.linkedin.com/pub/robert-onulak/12/2a1/564" target="_blank">Robert Onulak</a>) of Team Nitronic's sister team, <a href="http://teamdiscotank.com/" target="_blank">Disco Tank</a>, whom made the game "<a href="http://news.digipen.edu/student-projects/solstice-featured-at-tokyo-game-shows-sense-of-wonder-night/#.VMzAjf54rNo" target="_blank">Solstice</a>".  We created the "Superdyne" architecture to be used by both teams.  Superdyne was additionally used in a couple of projects by team members.

Following is a list of most of Superdyne's features.  **Listed in bold** are the ones on which I was a significant part in creating.

"Too Long; Didn't Read" list of what I worked on: [Action list][], [internal hierarchical profiler][], [memory debugger][], [function binding][], [limited Lua binding][], [RPC and the ToolServer][], [C++ Reflection][], and [Serialization][].

<ul>
	<li id="li-action-list"><strong>Action List:</strong> Alternative to a state machine for describing behavior.  Every act() call executes the first action found in the first non-blocked group.  Execution continues until no more non-blocked actions are available.  Groups can be blocked/unblocked/modified while the list is executing.</li>
	<br/>
	<li>Containers:
		<ul>
			<li>Handles: Used primarily by <em>GameObjectHandle</em>.</li>
			<li><strong><em>RefString:</em></strong> Holds only pointers to a <em>printf</em>-style format and arguments.  This is used to avoid needing a temporary, local buffer to write into, only to be written into the actual destination buffer shortly thereafter.</li>
			<li><strong>Templated Static Array:</strong> Basic static array with some out-of-bound access protection.</li>
			<li><strong>String:</strong> <a href="http://en.wikipedia.org/wiki/Object_copy#Lazy_copy" target="_blank">Late-copy</a> string.  We still primarily used <em>std::string</em> in most game code, though.</li>
		</ul>
	</li> <!-- /containers li -->
	<br/>
	<li>Core: Handles program state, ISystem registration, frame-rate control, and game pause/unpause.</li>
	<br/>
	<li>Debugging macros: Provides build-based compiled-out macros such as DebugErrorIf and ReleaseErrorIf.  Also had severity-based error and warning macros such as <em>gerror</em>; these were mostly glorified <em>fprintf</em> wrappers.</li>
	<br/>
	<li>Client Variable: Very similar to <a href="http://en.wikipedia.org/wiki/CVAR" target="_blank">Quake's CVAR system</a>.  A global place to register variables fo any basic type (plus strings) for access in another area.  These can also be flagged as data to be saved in a per-user file.</li> <!-- /cvar li -->
	<br/>
	<li id="li-internal-hierarchical-profiler"><strong>Internal, Hierarchical Profiler:</strong> Alternative to an existing profiler in Superdyne.  Can write out all profiled information for a given frame, or just "spike" frames where a drop in performance beyond a specified threshold occurs.  In Nitronic Rush, this was set to print debug information to the screen on any spike frame, where it listed which profiled items were most to blame.  This profiler is nearly identical to a homework assignment in <a href="https://www.digipen.edu/coursecatalog/#CS391" target="_blank">CS391: "Code Analysis and Optimization"</a> at <a href="https://digipen.edu" target="_blank">DigiPen</a>.</li> <!-- /internal-hierarchical-profiler li -->
	<br/>
	<li id="li-memory-debugger"><strong>Memory Debugger:</strong> Can replace all allocations globally, or just specific ones.  Immediately detects any overflow or underflow read/write attempts.  Uses Windows OS features to do this (and consumes a great deal of memory in doing so; two pages per allocation it watches).  Drop-in copy from an assignment for <a href="https://www.digipen.edu/coursecatalog/#CS391" target="_blank">CS391: "Code Analysis and Optimization"</a> at <a href="https://digipen.edu" target="_blank">DigiPen</a>.</li> <!-- /memory-debugger li -->
	<br/>
	<li><strong><em>PrintLastOsError()</em>:</strong> Just prints to stderr the last Windows error message.  Because doing this manually is tedious.</li>
	<br/>
	<li>Factory: Creates <em>GameObjects</em> based on "blueprints".  I worked on two of the three implementations of blueprints and serialization we used with the Factory over the course of the primary projects using Superdyne.</li>
	<br/>
	<li id="li-function-binding"><strong>Template-Based Function Binding:</strong> Written towards the start of my Sophomore year at <a href="https://digipen.edu" target="_blank">DigiPen</a>.  Used by <a href="http://www.youtube.com/watch?v=HWbWmxL7GxA" target="_blank">bLight</a> (Sophomore year team project), Superdyne, and <a href="http://www.youtube.com/watch?v=lgDnPDxZLjM&t=37s" target="_blank">Fragment</a> (another Junior year project, but one I had no other part in).  This system was extremely useful for Action Lists, our message systems, and property reflection.  However, this implementation is a hefty amount of code that is not trivial to read or follow.  If a compilation error occurs involving it, figuring out what's wrong can be challenging.  I'm also no longer satisfied by its speed.  The general idea works well -- this implementation is somewhat similar to what <a href="http://thatgamecompany.com/games/flow/" target="_blank">flOw</a> by <a href="http://thatgamecompany.com/" target="_blank">thatgamecompany</a> used -- but it should be preferably re-written before being used again.</li> <!-- /function-binding li -->
	<br/>
	<li><em>GameObject</em>, <em>ComponentManager</em>, and <em>Component</em>: Game objects can have as many components as desired, and even multiples of the same type.  Components are automatically registered/unregistered with their respective managers on <em>GameObject</em> initialization/de-initialization.  If you just want a component to be updated once each frame, a special <em>UpdateComponent</em> is available to inherit from.</li> <!-- /components li -->
	<br/>
	<li><em>Level</em>, <em>GameStateManager</em>: <em>GameStateManager</em> switches between <em>Level</em>s when requested, or quits the game.</li>
	<br/>
	<li><em>GhostEngine</em>: <a href="http://www.audiokinetic.com/en/products/wwise/introduction" target="_blank">Wwise</a>-based audio engine.</li>
	<br/>
	<li>Input: Uses <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/ee417014(v=vs.85).aspx" taret="_blank">XInput</a> for gamepads, and RawInput for keyboard, mouse, and 3D mouse support.  Differentiates between developer input and user input for easy toggling on/off of developer hotkeys in one location.</li>
	<br/>
	<li><em>Interpolator</em>, <em>PolyInterpolator</em>, <em>SplineSystem</em>: Templated, pausable variable interpolators</li>
	<br/>
	<li id="li-lua-binding"><strong><a href="http://www.lua.org/" target="_blank">Lua</a> binding:</strong> For my own part, I mostly wrapped up the Lua state in a nicer C++-style interface, and used a mix of tolua++ and my own function binding for binding to Lua.  This old system is barely in use.  <a href="/projects/nitronic-rush">Nitronic Rush</a> in particular uses almost no Lua.  In earlier stages of development, our level file was just a Lua script written by a <a href="http://www.blender.org/" target="_blank">Blender</a> "exporter" script that would create and modify all the level objects.  A newer Lua binding system was written by <a href="http://www.linkedin.com/pub/robert-onulak/12/2a1/564" target="_blank">Robert Onulak</a>, based on <a href="http://thatgamecompany.com/company/people/john-edwards/" target="_blank">John Edwards</a> of <a href="http://thatgamecompany.com/" target="_blank">thatgamecompany</a>'s template meta-programming lecture.</li> <!-- /lua-binding li -->
	<br/>
	<li>Math library: Matrices, vectors, quaternions, and some basic AABB-oriented classes.  Physics and graphics were not part of Superdyne, so only the most basic, shared math is implemented here.  By the end, because of the shared <em>Transform</em> component yet fairly different uses of it between the two games, that component ended up being fairly bloated.</li>
	<br/>
	<li><strong><em>MessageSystem</em></strong>, and <em>IMessage</em>: An underlying template-based function-bound message system, with an object-based top layer.  The underlying function binding is my old system from the Sophomore year.  Used by four games in total.</li>
	<br/>
	<li id="li-rpc-toolserver"><strong>RPC and the <em>ToolServer</em></strong>: We only used this towards the start of our projects.  At its peak, it allowed remote procedure calls on a one-to-one basis.  Lua was one of the possible receivers, which was very handy for quickly trying things out on a game.  Originally it was intended to allow levels to be edited by our designer while people were play-testing.  In the end, the most memorable things it allowed were faster iteration on some scripts (mostly for <a href="http://news.digipen.edu/student-projects/solstice-featured-at-tokyo-game-shows-sense-of-wonder-night/#.VMzAjf54rNo" target="_blank">Solstice</a>), and launching Minecraft on someone else's machine.  We just didn't have much need for this.</li> <!-- /rpc li -->
	<br/>
	<li id="li-cpp-reflection"><strong>C++ Reflection</strong>: Four versions of it.  The oldest reflection system was from Sophomore year, and based on the template-based function binding code from that year.  The second was in use only briefly, while we tinkered with the possibility of using <a href="http://www.wxwidgets.org/" target="_blank">wxWidgets</a>.  It had special considerations like proxy-ing the actual data being modified, and the ability for data to refuse a change that wasn't valid.  The third was based on <a href="http://thatgamecompany.com/company/people/john-edwards/" target="_blank">John Edwards</a> of thatgamecompany's template meta-programming lecture.  The final one (used today to populate <a href="http://www.antisphere.com/Wiki/tools:anttweakbar" target="_blank">AntTweakBar</a> bars for the level editor in <a href="/projects/nitronic-rush">Nitronic Rush</a>) is a super straight-forward <a href="http://en.wikipedia.org/wiki/Visitor_pattern" target="_blank">visitor-style</a> interface.  This can be used well for things like serialization and debug output, as well.  It has some specializations for common math types in Superdyne, and doesn't have the code generation overhead or potentially confusing compiler error messages the template-based reflection had.</li> <!-- /c++-reflection li -->
	<br/>
	<li id="li-serialization"><strong>Serialization</strong>: Three versions of it.  Originally tried to just use <a href="http://xerces.apache.org/xerces-c/" target="_blank">Xerxes-C++ Parser</a>.  This ended up being a terrible idea, as Xerxes feels more aimed at business applications (it's very strict and good at verifying XML data).  Second was a very brief play with <a href="http://www.json.org/" target="_blank">JSON</a>.  Finally, ended with the "Superial" (<em>Super</em>dyne <em>serial</em>ization) system.  Uses <a href="http://www.grinninglizard.com/tinyxml/" target="_blank">TinyXML</a> to parse our XML data (mostly level files and game object "blueprints"; TinyXML because it's small and good for games).  Once TinyXML parses the data, I move it over into a <em>SuperialDataMap</em>, made up of <em>SuperialValues</em>.  "Superial" covers a smaller set of features than XML, but plenty for our purposes.  <em>SuperialValues</em> are the primary means of passing data around to components being serialized.  <a href="http://www.linkedin.com/pub/robert-onulak/12/2a1/564" target="_blank">Robert Onulak</a> wrote another layer on top of Superial to simplify working with it.  This hides more features, but the underlying Superial data can still be accessed when those features are needed.</li> <!-- /serialization li -->
	<br/>
	<li>Singleton: Template-based means of defining a singleton type and its "lifetime policy".</li>
	<br/>
	<li>Basic threading library: <em>Thread</em>, <em>Mutex</em>, <em>Lock</em>, <em>ActiveObject</em>, <em>ThreadPool</em>, and <em>WorkerThread</em> types.  Not used by <a href="/projects/nitronic-rush">Nitronic Rush</a>.</li>
</ul>

[Nitronic Rush]: /projects/nitronic-rush
[action list]: #li-action-list
[internal hierarchical profiler]: #li-internal-hierarchical-profiler
[memory debugger]: #li-memory-debugger
[function binding]: #li-function-binding
[limited lua binding]: #li-lua-binding
[rpc and the toolserver]: #li-rpc-toolserver
[c++ reflection]: #li-cpp-reflection
[serialization]: #li-serialization
