#...initialize looping variable, assume 'yes' as the first answer
$continueYN = "y";

print "What's your name?\n";
$usrName = <STDIN>;
chomp($usrName);
 
while ($continueYN eq "y")
{
	
	print $usrName.", we can now convert temperatures both ways. \nTo convert from F to C, enter 'F'.\nTo convert from C to F, enter 'C'.\n";
	$conversion = <STDIN>;
	chomp($conversion);
	
	if ($conversion eq "f" || $conversion eq "F") {
		#...get temperature input from the user
		print $usrName.", enter next temperature in degrees Farenheight (F):";

		$degreeF = <STDIN>;
		chomp($degreeF);

		#...convert temperature from F to Celsius
		$degreeC = int(($degreeF - 32) * 5 / 9);

		print $usrName.", temperature in degrees F is: ".$degreeC."\n";

		#...check for temperature below freezing..
		if ($degreeF < 32)
		{
			print $usrName.", pack long underwear!\n";
		}

		#...check for it being a hot day...
		if ($degreeC > 85)
		{
			print $usrName.", remember to hydrate!\n";
		}

		print "Input another?";

		$continueYN = <STDIN>;
		chomp($continueYN);
	
	} elsif ($conversion eq "c" ||  $conversion eq "C" ) {
		#...get temperature input from the user
		print $usrName.", enter next temperature in degrees Celsius (C):";

		$degreeC = <STDIN>;
		chomp($degreeC);

		#...convert temperature from F to Celsius
		$degreeF = int(($degreeC * 9 / 5) + 32);

		print $usrName.", temperature in degrees C is: ".$degreeF."\n";

		#...check for temperature below freezing..
		if ($degreeF < 32)
		{
			print $usrName.", pack long underwear!\n";
		}

		#...check for it being a hot day...
		if ($degreeF > 100)
		{
			print $usrName.", remember to hydrate!\n";
		}
		
			print "Input another?";

		$continueYN = <STDIN>;
		chomp($continueYN);
	} else {
	
		print $usrName.", we can now convert both ways. \nTo convert from F to C, enter 'F'.\nTo convert from C to F, enter 'C'.\n";
		$conversion = <STDIN>;
		
	}
	
	
}