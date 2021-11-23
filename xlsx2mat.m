tabla = readtable('output/waypoints_matlab.xlsx');
fp=table2struct(tabla);
save('output/fp.mat','fp')