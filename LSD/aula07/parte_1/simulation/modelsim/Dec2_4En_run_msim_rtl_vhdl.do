transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vcom -93 -work work {C:/Users/Ruben/Documents/UA/UA_rep/LSD/aula07/parte_1/Dec2_4En.vhd}

