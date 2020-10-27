# Comandos de la Práctica 01
## Victor Manuel Serrato Solano

# Parte I. 

**Respuesta 1:**

/bin/bash 

**Respuesta 2:**

mkdir -p {data,filtered,raw_data,meta,scripts,figures,archive}

**Respuesta 3:**

mv -t data filtered/ raw_data/

**Respuesta 4:**

La organización se debe a que nos ayuda a entender lo que se está haciendo, entender cuales son los datos crudos, datos procesados, scripts y la documentación.

* **data:** Es el que contiene lo datos.

* **raw_data:** Son los datos en crudo.

* **filtered:** Datos ya modificados y/o procesados.

* **meta:** Donde se guardan los metadatos.

* **scrips:** Aquí se guardan los scripts que creamos para el análisis de los datos.

* **figures:** Es opcional y sólo es para los scripts que hacen las figuras.

* **archive:** Es un directorio que es para borradores o cosas que no vamos a necesitar pero que ya hicimos, no se debe subir al repositorio.

# Parte II.

**Respuesta 1:**

chmod +x delay.sh

**Respuesta 2:**

ls -lth

./delay.sh

**Respuesta 3:**

sleep 30

**Respusta 4:**

kill -9 353

# Parte III.

**Respuesta 1:**

mv sequence.fasta sarscov2_genome.fasta
mv sequence.gff3 sarscov2_genome.gff3

**Respuesta 2:**

mv sequence.fasta splike_c.faa
mv sequence\ \(1\).fasta splike_b.faa
mv sequence\ \(2\).fasta splike_a.faa

mv -p /home/GenomicaComputacional/vserrato_p01/data/raw_data {sarscov2_genome.fasta,sarscov2_genome.gff3,splike_c.faa,splike_b.faa,splike_a.faa,SRR10971381_R1.fastq.gz,SRR10971381_R2.fastq.gz,sarscov2_assembly.fasta.gz}

# Parte IV.

**Respuesta 1:**

ln -s ~/GenomicaComputacional/vserrato_p01/data/raw_data/splike_c.faa
ln -s ~/GenomicaComputacional/vserrato_p01/data/raw_data/splike_b.faa
ln -s ~/GenomicaComputacional/vserrato_p01/data/raw_data/splike_a.faa

**Respuesta 2:**

touch glycoproteins.faa

**Respuesta 3:**

==> splike_a.faa <==
>pdb|6VXX|A Chain A, SARS-CoV-2 spike glycoprotein

==> splike_b.faa <==
>pdb|6VXX|B Chain B, SARS-CoV-2 spike glycoprotein

==> splike_c.faa <==
>pdb|6VXX|C Chain C, SARS-CoV-2 spike glycoprotein

**Respuesta 4:**

cat splike_*.faa > glycoproteins.faa

**Respuesta 5:**

mv splike_*.faa ../../archive/

Las ligas suaves ya no apuntan a nugun archivo porque sigue la misma referencia

**Respuesta 6:**

less sarscov2_genome.fasta | head -3
>NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA
CGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAAC

zless sarscov2_assembly.fasta.gz | head -3
>NODE_1_length_264_cov_161.042781
CACAAATCTTAACACTCTTCCCTACACGACGCTCTTCCGATCTACGCCGGGCCATTCGTA
CGAACCGATACCTGTGGTAAAGGGTCCTACTGTATGGTGGTACACGAGTAGTAGCAAATG

La diferencia es que uno es completo y el va por nodos

**Respuesta 7:**

less sarscov2_genome.fasta | grep -c ">"
1

zless sarscov2_assembly.fasta.gz | grep -c ">"
35

**Respuesta 8:**

zless SRR10971381_R2.fastq.gz | head -12
@SRR10971381.512_2
CGTGGAGTATGGCTACATACTACTTATTTGATGAGTCTGGTGAGTTTAAAGTGGCTTCACATATGTATTGTTCTTTCTACCCTCCAGATGAGGATGAAGAAGAAGGTGATTGTGAAGAAGAAGAGTTTGAGCCATCAACTCAATATGAGT
+
/FFFA/A/FFFF66FFFFFF/FF/FFFFFFFFFFFFF/AFFF6FFFA6FFFFF/FFFFFFFFFFFFFFFFFF/FF/FFFFFA/FFF/FFF/A/AFA/FFFFF/=F/F/F/AFAFF//A/AFF//FFAF/FFF=FFAFFFA/A/6=///==
@SRR10971381.556_2
TTTGTAAAAATAAAATAAAAAAAATAAAAATAATATATTAAAAAAAGATAAATAAAAAAATGAACAATTAATAAAAAAAAAAAAAAAAAAAAATTAAAAAAAAAAAAAAAAAAAATAAAAAAAAAAAAAAATAAAAAAAAAATTATAAAA
+
6AFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF/FFFAFFFFFF/FFA/FF=F//=FF/FFFFFFFFFFFFFA/FFFF/FF/FA//F/FFFFFFA/=FFFFF/FFFF/F=FFFAFF///FFFFA/FF/6//////=/
@SRR10971381.1428_2
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
+
FFFFFFFFFFFFAFFFAFFFFFF6A//F//FFF

El patrón que encontré es que siempre hay un + que los divide 

zless SRR10971381_R2.fastq.gz | grep -c "+"
130022

**Respuesta 9:**

* fasta: Contiene la secuencia completa, nucleotidos
* fastq: Va por separando los nucleotidos
* faa: son amnoacidos FASTA

**Respuesta 10:**

-S hace que todo el texto aparezca en una sola linea para reconocer el formato

**Respuesta 11:**

awk '{print $3}' sarscov2_genome.gff3 | grep -c "gene"
11

De acuerdo a los visto corresponde a regiones y "gene" es un gen pero "CDS" parece ser una parte especifica del gen.

#Ejercicio Extra

**Respuesta 1:**

sort sarscov2_genome.gff3 | awk '{print $3}' | uniq -c > barplot_data.txt