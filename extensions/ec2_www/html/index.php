<!DOCTYPE html>
<html>
<head>
<style type="text/css">
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
#chart-container {
  width: 640px;
  height: auto;
}
</style>
</head>

<body>
<?php
	require ("../db_inc.php");

	$DB = new Data ();
?>


<section>
	<h1>Normal User log: </h1>
<?php
	$DB->get_user ();
	$data = []; 
	foreach ($DB->result as $row) {
		if (array_key_exists ($row["username"], $data))
			$data[$row["username"]] ++;
		else
			$data[$row["username"]] = 1;
	}
	//print_r($data);
?>
<img src=info.php>
</section>
<section>
	<h1>Unknown User log: </h1>
<?php
	$DB->get_baduser ();
	//print json_encode ($data, JSON_PRETTY_PRINT);
?>
</section>

</body>
</html>
<img src=
>
