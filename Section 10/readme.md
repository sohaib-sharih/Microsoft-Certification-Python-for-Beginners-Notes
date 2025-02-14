<h1>Python Functions</h1>
    <ol type="1">
        <li>A function always returns values, and sometimes it may have <b>required</b> or <b>optional inputs.</b> to return a value.</li>
        <li>The inputs we take for functions are usually called <b>arguments</b> and <b>parameters</b>, but in this lesson we will refer to it as <b>arguments.</b> </li>
        <li>You can create a function using <b>def nameOfFunction()</b>, then call it where ever in the program using nameOfFunction(). When you use <b>parenthesis()</b>, it means there are no arguments needed to call this function.</li>
        <li>If you define a function's statement implicitly, and save the value of output inside a variable, it will output NONE. If you explicitly return a value in a statement of the function, then save it inside a variable, the output will <b>change</b> and return the desired value.</li>
        <li><b>NOTE</b> to use a function's value, you need to <b>explicitly return a value.</b>. In Python, if a function doesn't explicitly return a value, it implicitly returns None.</li>
        <li><b>Built in Functions</b> are immediately available and don't need to <b>import them.</b> But some of these functions <b>require arguments</b>, and some function arguments are <b>optional.</b> <i>Example str('') will return an empty string if no argument is provided, where as any([]) requires atleast 1 argument, otherwise it will return an <b>error.</b></i></li>
        <li><b>Build functions that require arguments</b>; these functions require arguments so you can build conditional functions. </li>
        <li><b>Catch all condition</b> <i>Where if a condition is <b>true</b> then the condition will print the statement, <b>else</b> if the value of argument differs, then the else statement will run. And if there is no argument, then it will give a <b>typeerror</b></i> functions example: <br>
        <img src="/images/10a.PNG" alt=""></li>
        <li><b>Multiple arguments</b> can be used separated by simple comma.</li>
        
</ol>

<h1>Use Keyword Arguments</h1>
    <ol type="1">
        <li><b>Keyword arguments</b> allows you to define a value of an argument by default within the function. Example def timeA(destination, hours=33). <i>This allows you to make that <b>argument</b> optional.</i></li>
        
</ol>

<h1>Variable Arguments</h1>
    <ol type="1">
        <li><b>Variable Arguments</b> are used when you want the function you created to accept infinite number of arguments, you can do so by adding an Aesterik before the <b>args</b> variable name. <b>Note</b> the name of the variable can be anything else as well, but args is what most developers use, and is the convention.</li>
        <li>example: <br>
        <img src="/images/10b.PNG" alt=""></li>
        <li><b>Keyword Arguments</b> these can be used in a similar way, except with double asteriks, as shown below. <br>
        <img src="/images/10c.PNG" alt=""></li>
        <li>Example 2 of <b>keyword arguments</b> <br>
        <img src="/images/10d.PNG" alt=""></li>
        <li><b>Excercise:</b><br>
        <img src="/images/10e.PNG" alt=""><br>
    <img src="/images/10f.PNG" alt=""></li>
</ol>