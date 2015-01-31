As part of working on [Nitronic Rush][], I worked with another technical director/architect (<a href="http://www.linkedin.com/pub/robert-onulak/12/2a1/564" target="_blank">Robert Onulak</a>) of Team Nitronic's sister team, <a href="http://teamdiscotank.com/" target="_blank">Disco Tank</a>, whom made the game "<a href="http://news.digipen.edu/student-projects/solstice-featured-at-tokyo-game-shows-sense-of-wonder-night/#.VMzAjf54rNo" target="_blank">Solstice</a>".  We created the "Superdyne" architecture to be used by both teams.  Superdyne was additionally used in a couple of projects by team members.

Following is a list of most of Superdyne's features.  **Listed in bold** are the ones on which I was a significant part in creating.

"Too Long; Didn't Read" list of what I worked on: [Action list][], [internal hierarchical profiler][], [memory debugger][], [function binding][], [limited Lua binding][], [RPC and the ToolServer][], [C++ Reflection][], and [Serialization][].

<ul>
	<li id="li-action-list"><strong>Action List:</strong> Alternative to a state machine for describing behavior.  Every act() call executes the first action found in the first non-blocked group.  Execution continues until no more non-blocked actions are available.  Groups can be blocked/unblocked/modified while the list is executing.</li>
	<li>Containers:
		<ul>
			<li>Handles: Used primarily by <em>GameObjectHandle</em>.</li>
			<li><strong><em>RefString:</em></strong> Holds only pointers to a <em>printf</em>-style format and arguments.  This is used to avoid needing a temporary, local buffer to write into, only to be written into the actual destination buffer shortly thereafter.</li>
			<li><strong>Templated Static Array:</strong> Basic static array with some out-of-bound access protection.</li>
			<li><strong>String:</strong> <a href="http://en.wikipedia.org/wiki/Object_copy#Lazy_copy" target="_blank">Late-copy</a> string.  We still primarily used <em>std::string</em> in most game code, though.</li>
		</ul>
	</li> <!-- /containers li -->
	<li>Core: Handles program state, ISystem registration, frame-rate control, and game pause/unpause.</li>
	<li>Debugging macros: Provides build-based compiled-out macros such as DebugErrorIf and ReleaseErrorIf.  Also had severity-based error and warning macros such as <em>gerror</em>; these were mostly glorified <em>fprintf</em> wrappers.</li>
	<li>Client Variable: Very similar to<a href="http://en.wikipedia.org/wiki/CVAR" target="_blank">Quake's CVAR system</a>.  A global place to register variables fo any basic type (plus strings) for access in another area.  These can also be flagged as data to be saved in a per-user file.</li> <!-- /cvar li -->
	<li id="li-internal-hierarchical-profiler"><strong>Internal, Hierarchical Profiler:</strong> Alternative to an existing profiler in Superdyne.  Can write out all profiled information for a given frame, or just "spike" frames where a drop in performance beyond a specified threshold occurs.  In Nitronic Rush, this was set to print debug information to the screen on any spike frame, where it listed which profiled items were most to blame.  This profiler is nearly identical to a homework assignment in <a href="https://www.digipen.edu/coursecatalog/#CS391" target="_blank">CS391: "Code Analysis and Optimization"</a> at <a href="https://digipen.edu" target="_blank">DigiPen</a>.</li> <!-- /internal-hierarchical-profiler li -->
	<li id="li-memory-debugger"><strong>Memory Debugger:</strong> Can replace all allocations globally, or just specific ones.  Immediately detects any overflow or underflow read/write attempts.  Uses Windows OS features to do this (and consumes a great deal of memory in doing so; two pages per allocation it watches).  Drop-in copy from an assignment for <a href="https://www.digipen.edu/coursecatalog/#CS391" target="_blank">CS391: "Code Analysis and Optimization"</a> at <a href="https://digipen.edu" target="_blank">DigiPen</a>.</li> <!-- /memory-debugger li -->
	<li><strong><em>PrintLastOsError()</em>:</strong> Just prints to stderr the last Windows error message.  Because doing this manually is tedious.</li>
	<li>Factory: Creates <em>GameObjects</em> based on "blueprints".  I worked on two of the three implementations of blueprints and serialization we used with the Factory over the course of the primary projects using Superdyne.</li>
	<li id="li-function-binding"><strong>Template-Based Function Binding:</strong> Written towards the start of my Sophomore year at <a href="https://digipen.edu" target="_blank">DigiPen</a>.  Used by <a href="http://www.youtube.com/watch?v=HWbWmxL7GxA" target="_blank">bLight</a> (Sophomore year team project), Superdyne, and <a href="http://www.youtube.com/watch?v=lgDnPDxZLjM&t=37s" target="_blank">Fragment</a> (another Junior year project, but one I had no other part in).  This system was extremely useful for Action Lists, our message systems, and property reflection.  However, this implementation is a hefty amount of code that is not trivial to read or follow.  If a compilation error occurs involving it, figuring out what's wrong can be challenging.  I'm also no longer satisfied by its speed.  The general idea works well -- this implementation is somewhat similar to what <a href="http://thatgamecompany.com/games/flow/" target="_blank">flOw</a> by <a href="http://thatgamecompany.com/" target="_blank">thatgamecompany</a> used -- but it should be preferably re-written before being used again.</li> <!-- /function-binding li -->
	<li><em>GameObject</em>, <em>ComponentManager</em>, and <em>Component</em>: Game objects can have as many components as desired, and even multiples of the same type.  Components are automatically registered/unregistered with their respective managers on <em>GameObject</em> initialization/de-initialization.  If you just want a component to be updated once each frame, a special <em>UpdateComponent</em> is available to inherit from.</li> <!-- /components li -->
	<li><em>Level</em>, <em>GameStateManager</em>: <em>GameStateManager</em> switches between <em>Level</em>s when requested, or quits the game.</li>
	<li><em>GhostEngine</em>: <a href="http://www.audiokinetic.com/en/products/wwise/introduction" target="_blank">Wwise</a>-based audio engine.</li>
	<li>Input: Uses <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/ee417014(v=vs.85).aspx" taret="_blank">XInput</a> for gamepads, and RawInput for keyboard, mouse, and 3D mouse support.  Differentiates between developer input and user input for easy toggling on/off of developer hotkeys in one location.</li>
	<li><em>Interpolator</em>, <em>PolyInterpolator</em>, <em>SplineSystem</em>: Templated, pausable variable interpolators</li>
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
