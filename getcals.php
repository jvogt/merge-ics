<?php
include 'config.php';
$date = new DateTime();
$ts = $date->getTimestamp();
$work_dir = "{$install_dir}/work";
function getfile($url,$tempname,$finalname) {
	global $work_dir;
	$_finalname = "{$work_dir}/cals/{$finalname}";
	$_tempname = "/tmp/${tempname}-${finalname}";
	$cmd = "wget ${url} -O {$_tempname}";
	exec($cmd,$output,$retval);
	if($retval == 0) {
		rename("{$_tempname}","{$_finalname}");
	}
}
foreach($files as $file) {
	getfile($file[1],$ts,$file[0]);
}
exec("{$install_dir}/merge_ics.py");
$cal = file_get_contents("{$work_dir}/cal.ics");
echo $cal;
?>
