tabla = readtable('waypoints.xlsx');
fp=table2struct(tabla);
save('fp.mat','fp')