#!/bin/bash

WD="WORKDIR"
GROUP="21"
echo "creating working directory"
if [ -d $WD ]; then
    echo "working directory already exists. It will be deleted and recreated";
    rm -rf $WD
    mkdir $WD
else
    mkdir "WORKDIR"
    echo "$WD directory is created"
fi
echo "copying the library in $WD"
cp -R mylib $WD
cd $WD/mylib
rm -rf __py*
rm -rf .ip*
cd -
echo "copying the INSTRUCTIONS.txt in $WD"
cp INSTRUCTIONS.txt $WD
echo "copying the report in $WD"
cp DM_report.pdf $WD
echo "copying the requirements.txt in $WD"
cp requirements.txt $WD
echo "creating the folder structure in $WD"
cd $WD
mkdir DM_${GROUP}_TASK{1..4}
mkdir -p datasets/customer
echo "folder structure created"
echo "renaming the report"
mv DM_report.pdf "DM_Report_${GROUP}.pdf"
echo "copying the customer_supermarket dataset"
cp ../datasets/customer/customer_supermarket.csv ./datasets/customer
echo "copying the spmf.jar library"
cp ../4*/spmf.jar DM*4
echo "copying the notebooks"
cd ..
cp 1.*/*.ipynb $WD/*1
cp 2.*/*.ipynb $WD/*2
cp 3.*/*.ipynb $WD/*3
cp 4.*/*.ipynb $WD/*4
echo "copyint the images in folder 4"
mkdir  $WD/DM_21_TASK4/products_imgs
cp 4.*/products_imgs/*  $WD/DM_21_TASK4/products_imgs
echo "notebooks copied"
cd $WD
echo "renaming the notebooks"
echo "TASK1"
cd DM*1
mv DP.ipynb datapreparation.ipynb
echo "DP.ipynb -> datapreparation.ipynb"
mv DU* dataunderstanding.ipynb
echo "DU.ipynb -> dataunderstanding.ipynb"
cd ..
echo "TASK2"
cd DM*2
mv CA* clusteringanalysis.ipynb
echo "CA.ipynb -> clusteringanalysis.ipynb"
cd ..
echo "TASK3"
cd DM*3
mv PA* predictiveanalysis.ipynb
echo "PA.ipynb -> predictiveanalysis.ipynb"
cd ..
echo "TASK4"
cd DM*4
mv SPM.ipynb sequentialpatternmining.ipynb
echo "SPM.ipynb -> sequentialpatternmining.ipynb"
cd ..
echo "notebooks renamed"

echo "Creating the archive"
echo "creating zip file"
zip -r "DM_${GROUP}.zip" DM* INSTRUCTIONS.txt mylib datasets requirements.txt "DM_Report_${GROUP}.pdf"
echo "zip file created"
echo "copying zip file to parent folder"
cp *zip ..
cd ..
echo "cleaning up"
rm -rf $WD
echo "DONE"


