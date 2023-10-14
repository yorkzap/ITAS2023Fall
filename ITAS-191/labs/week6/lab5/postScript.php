<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Magical Book of Backend</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11/build/highlight.min.js"></script>
    <style>
        .reveal {
            cursor: pointer;
            color: #007BFF;
        }

        .reveal:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <div class="container-fluid mt-3">
        <div class="row">
            <p>
                <?php
                if (isset($_POST) && !empty($_POST)) {
                    $formData = $_POST;
                    $firstName = htmlspecialchars($formData["firstname"]);
                    $lastName = htmlspecialchars($formData["lastname"]);

                    echo "Hey there, {$firstName} {$lastName}! 👋 <br>";
                    echo "Bravo for reaching this phase of your digital adventure!<br>";
                    echo "Every coder faces challenges, but it's your grit and determination that makes all the difference. <br>";
                    echo "And hey, if you can read the server's thoughts with this output, imagine what else you're capable of?<br>";
                    echo "Here is how the computer can use the form data to do cool stuff. Try to click any data below and observe what happens.<br>";
                    echo "Try to find the ITAS easter egg<br>";
                } else {
                    echo "No data received. Please recheck.";
                }
                ?>
            </p>
        </div>
        <div class="row">
            <?php
            if (isset($_POST) && !empty($_POST)) {
                echo "<table class='table table-bordered table-hover'>";
                echo "<thead><tr><th>Key</th><th>Value</th></tr></thead>";
                echo "<tbody>";
                foreach ($formData as $key => $value) {
                    $value = htmlspecialchars($value);
                    echo "<tr><td>" . ucwords($key) . "</td><td><span class='reveal' onclick='revealStory(this)'>{$value}</span></td></tr>";
                }
                echo "</tbody>";
                echo "</table>";
            } else {
                echo "<pre><code>The magical book awaits your tales...</code></pre>";
            }
            ?>
        </div>
    </div>
    <script>
        function revealStory(element) {
            let stories = {
                "firstname": "In the digital kingdom, this name is sung by the bytes in harmonious tunes.",
                "lastname": "This is the Easter Egg 1. If you find total 5, you win $500 at the end of your ITAS journey! Take a picture of this and email it to raj.singh@itas.ca with your name and program to claim.",
                //... you can add more custom stories for other keys
            };
            let key = element.parentElement.previousElementSibling.innerText.toLowerCase();
            alert(stories[key] || "This data enchants the wires, weaving its own mysterious spell.");
        }

        hljs.highlightAll();
    </script>
</body>

</html>
