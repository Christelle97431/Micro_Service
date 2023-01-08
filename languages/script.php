<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'http://127.0.0.1:5000/register',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => 'username={username}&email={email}&password={passord}&password_confirmation={password_confirmation}',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/x-www-form-urlencoded',
    'Cookie: session=.eJzVjUEKgzAUBa_y-lctZOG2XfYWRUWCvkYh-CE_0YXk7i09g5uuBgaGOWR4R28zTR7tIchfiJVxpJk4eSa_qcOmxdCVpqHPNHBNDIvl9FP3K28X6as7PX9pgU9E1BA4OeyMEZOuxB_--voBS4x3gg.Y59hPA.eISL2EdX9IZ5wgOc6iLSYAsyhHU'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
