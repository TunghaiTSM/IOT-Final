<?php
class Data {
	var $PASS = "tL738x7BX9RqWL6";
	var $USER = "admin";
	var $HOST = "mqtt.cv04k5yhpw98.us-east-1.rds.amazonaws.com";
	var $DBNAME = "MQTT";

	// MySQL
	var $conn, $result;

	function __construct () {
		mysqli_report (MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
		$this->conn = new mysqli ($this->HOST, $this->USER, $this->PASS, $this->DBNAME);
		$this->conn->set_charset ('utf8mb4');

		if ($this->conn->connect_error) die (
			"Connection failed: ". 
			$this->conn->connect_error
		);
	}

	var $Schema = [
		"username"=>"username",
		"photo"=>"photo",
		"time"=>"time",
		"id"=>"id",
	];


	function get_user () {

                $sql = "select * from identify where username!='Unknown' AND DATE(time)>=DATE_SUB(CURDATE(), INTERVAL 15 DAY) order by id ASC limit 15";
                $stmt = $this->conn->prepare ($sql);

                if (!$stmt->execute ()) {
                        echo "MySQL error, " . $stmt->error . "<br />";
                }

                $this->result = $stmt->get_result ();
                $this->displayTable (
                        array_keys ($this->Schema),
                        $this->result
                );
        }
	
	function get_user_json () {

                $sql = "select * from identify where username!='Unknown' AND DATE(time)>=DATE_SUB(CURDATE(), INTERVAL 15 DAY) order by id ASC limit 15";
                $stmt = $this->conn->prepare ($sql);

                if (!$stmt->execute ()) {
                        echo "MySQL error, " . $stmt->error . "<br />";
                }

                $this->result = $stmt->get_result ();
        }
	function get_baduser () {

                $sql = "select * from identify where username='Unknown' AND DATE_FORMAT(time, '%Y-%m-%d')>=DATE_SUB(CURDATE(), INTERVAL 10 DAY) order by id ASC limit 15";
                $stmt = $this->conn->prepare ($sql);

                if (!$stmt->execute ()) {
                        echo "MySQL error, " . $stmt->error . "<br />";
                }

                $this->result = $stmt->get_result ();
                $this->displayTable (
                        array_keys ($this->Schema),
                        $this->result
                );
        }

	// Private utils
        function displayTable($headings, $result) {
                if ( ! is_array($headings) ) {
                        return false;
                }

                echo "<table>\n";
                echo "<tr>\n";
                foreach($headings as $heading) {
                        echo "<th>" . $heading . "</th>\n";
                }
                echo "</tr>\n";

                echo "<tbody>";
                while ($row = $result->fetch_assoc ()) {
                        echo "<tr>\n";
                        foreach($row as $data) {
                                echo "<td>" . $data . "</td>";
                        }
                        echo "</tr>\n";
                }
                echo "</tbody>\n";
                echo "</table>\n";
		return true;
        }
};
?>
