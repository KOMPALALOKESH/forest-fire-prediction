<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Forest Fire Probability</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&display=swap" rel="stylesheet">

    <style>
        body {
            background-color: rgba(0, 0, 0, 0.8);
            background-image: url('static/forest_fire1.jpg');
            height: 100%;
            width: 100%;
        }

        .form-group {
            margin-bottom: 10px;
            width: 25%;
            /* Set the width of each input to 100px */
            margin-right: 20px;
            /* Add right margin */
        }

        .form-label {
            display: block;
            font-weight: bold;
            color: white;
            padding-bottom: 10px;
            /* Set label color to white */
        }

        .form-row {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            /* Add bottom margin to separate rows */
            justify-content: center;
            gap: 50px;
        }

        input.line-input {
            font-size: 20px;
            border: none;
            border-bottom: 3px solid rgb(193, 193, 193);
            outline: none;
            padding: 5px 0;
            transition: border-color 0.3s, box-shadow 0.3s;
            background-color: transparent;
            width: 100%;
        }

        input.line-input:focus {
            border-color: coral;
            box-shadow: 0px 20px 20px -15px coral;
        }

        #myform {
            margin-bottom: 20px;
        }

        #predict {
            display: block;
            margin: 0 auto;
            background-color: coral;
            color: white;
            height: 50px;
            width: 100px;
            border-radius: 5px;
            margin-top: 50px;
            font-size: large;
            box-shadow: 10px 10px 20px -15px coral;
        }
    </style>
</head>

<body>
    # Forest Fire Prediction

    Forest fires are a devastating natural phenomenon that can occur under specific conditions. One crucial factor is temperature, as high temperatures increase the likelihood of ignition and rapid spread. Oxygen availability also plays a significant role, as it fuels the combustion process. Dry conditions with low humidity further exacerbate the risk, as moisture content in vegetation decreases, making it more susceptible to catching fire. The combination of these factors creates a volatile environment where even a small spark can lead to a destructive and uncontrollable forest fire.

    <form id="myform" method="POST">
        <div class="form-row">
            <div class="form-group">
                **Temperature in °C**
                <input type="text" name="temperature" id="temperature" placeholder="" class="line-input" />
            </div>

            <div class="form-group">
                **Oxygen in ppm**
                <input type="text" name="oxygen" id="oxygen" placeholder="" class="line-input" />
            </div>

            <div class="form-group">
                **Humidity**
                <input type="text" name="humidity" id="humidity" placeholder="" class="line-input" />
            </div>
        </div>
    </form>
    
    [Predict](#predict)
    
    ## Result
    ---
    [//]: # (The result will be displayed here)
    <h2 id="result" style="font-family: 'Caveat', cursive; font-size: 50px; color:whitesmoke; text-align: center;"></h2>

    <script type="text/javascript">
        $(function () {
            $("#predict").click(function () {
                event.preventDefault();
                var form_data = new FormData($("#myform")[0]);
                console.log(form_data);
                $.ajax({
                    type: "POST",
                    url: "/predict",
                    data: form_data,
                    contentType: false,
                    processData: false,
                })
                    .done(function (data, textStatus, jqXHR) {
                        $("#result").text(data);
                    })
                    .fail(function (data) {
                        alert("Error!");
                    });
            });
        });
    </script>
</body>

</html>
