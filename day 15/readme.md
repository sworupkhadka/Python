<h2>Resource Validation & Coffee Making</h2>

<h3>1. Checking Resource Availability</h3>

<pre><code>
for item in MENU[drink]['ingredients']:
    if MENU[drink]['ingredients'][item] > resources.get(item, 0):
        print(f"Sorry, there is not enough {item}.")
        return False
return True
</code></pre>

<p><strong>Purpose:</strong><br>
This block ensures that the machine has enough ingredients to make the selected drink.</p>

<p><strong>Breakdown:</strong></p>
<ul>
    <li><code>for item in MENU[drink]['ingredients']</code> → Loops through each ingredient needed for the drink.</li>
    <li><code>MENU[drink]['ingredients'][item]</code> → Amount of the ingredient required for the chosen drink.</li>
    <li><code>resources.get(item, 0)</code> → Current available amount in the machine (defaults to 0 if the ingredient doesn't exist).</li>
    <li><code>&gt;</code> → Checks if required amount exceeds available resources.</li>
    <li>If any ingredient is insufficient:
        <ul>
            <li>Prints a message informing the user which ingredient is lacking.</li>
            <li>Returns <code>False</code> to prevent the order from proceeding.</li>
        </ul>
    </li>
    <li>If all ingredients are sufficient, returns <code>True</code> so the coffee can be made.</li>
</ul>

<p><strong>Example:</strong><br>
If making a latte requires 200ml of water but only 100ml is available, the machine will print:</p>
<pre><code>Sorry, there is not enough water.</code></pre>

<hr>

<h3>2. Making Coffee & Deducting Resources</h3>

<pre><code>
for item in MENU[drink]['ingredients']:
    resources[item] -= MENU[drink]['ingredients'][item]
print(f"Here is your {drink} ☕. Enjoy!")
</code></pre>

<p><strong>Purpose:</strong><br>
This block deducts the used ingredients from the machine’s resources after successfully making a drink.</p>

<p><strong>Breakdown:</strong></p>
<ul>
    <li><code>for item in MENU[drink]['ingredients']</code> → Loops through each ingredient required.</li>
    <li><code>resources[item] -= MENU[drink]['ingredients'][item]</code> → Subtracts the required amount from the available resources.
        <ul>
            <li>Example: If espresso uses 50ml water and 18g coffee:
                <ul>
                    <li><code>resources['water'] -= 50</code></li>
                    <li><code>resources['coffee'] -= 18</code></li>
                </ul>
            </li>
        </ul>
    </li>
    <li><code>print(f"Here is your {drink} ☕. Enjoy!")</code> → Confirms to the user that their drink has been served.</li>
</ul>

<p><strong>Effect:</strong><br>
- Automatically updates the machine’s resource levels.<br>
- Provides a clear message to the user that their order is complete.</p>
