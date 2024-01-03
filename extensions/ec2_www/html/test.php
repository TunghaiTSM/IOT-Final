<?php
	require ("../db_inc.php");
	$DB = new Data ();
	$DB->get_user_json ();
	$data = []; 
	foreach ($DB->result as $row)
		$data[] = $row;

	// Count values and create a frequency array
	echo json_encode ($data);
//	$result = array_count_values ($data);
//	echo json_encode ($result);
?>
