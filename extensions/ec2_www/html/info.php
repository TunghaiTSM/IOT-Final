<?php 
	require ("../db_inc.php");
	$DB = new Data ();
	$DB->get_user_json ();
	$data = []; 
	foreach ($DB->result as $row) {
		if (array_key_exists ($row["username"], $data))
			$data[$row["username"]] ++;
		else
			$data[$row["username"]] = 1;
	}
include ("lib/jpgraph/src/jpgraph.php"); 
include ("lib/jpgraph/src/jpgraph_pie.php"); 
include ("lib/jpgraph/src/jpgraph_pie3d.php"); 
//$data = array(19,23,34,38,45,67,71,78,85,87,90,96); 
$graph = new PieGraph(400,300); 
$graph->SetShadow(); 
$graph->title->Set("System usage percentage."); 
$graph->title->SetFont(FF_SIMSUN,FS_BOLD); 
$pieplot = new PiePlot3D(array_values ($data)); //建立PiePlot3D物件 
$pieplot->SetCenter(0.4); //設定餅圖中心的位置 
$pieplot->SetLegends(array_keys ($data)); //設定圖例 
$graph->Add($pieplot); 
$graph->Stroke(); 
?> 
