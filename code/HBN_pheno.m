clear;
clc;
[num,txt,raw] = xlsread('/cis/home/sandhya/NDD/aut_pheno/9994_SCQ_20180927.xlsx');
SCQ = raw(:,[1 52]);
SCQ(2,:)=[];

[num,txt,raw] = xlsread('/cis/home/sandhya/NDD/aut_pheno/9994_ASSQ_20180927.xlsx');
ASSQ = raw(:,[1 39]);
ASSQ(2,:)=[];

[num,txt,raw] = xlsread('/cis/home/sandhya/NDD/aut_pheno/9994_SRS_20180927.xlsx');
SRS = raw(:,[1 91 92]);
SRS(2,:)=[];

[num,txt,raw] = xlsread('/cis/home/sandhya/NDD/aut_pheno/9994_SRS_Pre_20180927.xlsx');
SRSPre = raw(:,[1 91 92]);
SRSPre(2,:)=[];

% SRScom = [SRS;SRSPre];

scqdat = SCQ([2:end],2);
scqdat = cell2mat(scqdat);
histogram(scqdat)
title('SCQ data')
xlabel('Score')
ylabel('Number of Subjects')
xlim([0, inf])

assqdat = ASSQ([2:end],2);
assqdat = cell2mat(assqdat);
histogram(assqdat)
title('ASSQ data')
xlabel('Score')
ylabel('Number of Subjects')
xlim([0, inf])

srsdat = SRS([2:end],2);
srsdat = cell2mat(srsdat);
histogram(srsdat)
title('SRS data')
xlabel('Score')
ylabel('Number of Subjects')
xlim([0, inf])

srspredat = SRSPre([2:end],2);
srspredat = cell2mat(srspredat);
histogram(srspredat)
title('SRS Pre data')
xlabel('Score')
ylabel('Number of Subjects')
xlim([0, inf])