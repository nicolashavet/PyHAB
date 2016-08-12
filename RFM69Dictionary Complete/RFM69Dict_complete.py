# RFM69 Dictionary
#
# Ported to Micropython 2016 Ara Kourchians
#
# C code Author: Phil Crump (phildcrump@gmail.com)
# Copyright (C) 2014 Phil Crump
# Based on RF22.h
# Author: Mike McCauley (mikem@open.com.au)
# Copyright (C) 2011 Mike McCauley

registers = {
"RFM69_SPI_WRITE_MASK" : 0x80,

# This is the maximum message length that can be supported by this library. Limited by
# the single message length octet in the header. 
# Yes, 255 is correct even though the FIFO size in the RF22 is only
# 64 octets. We use interrupts to refill the Tx FIFO during transmission and to empty the
# Rx FIFO during reception
# Can be pre-defined to a smaller size (to save SRAM) prior to including this header
"RFM69_MAX_MESSAGE_LEN" : 64,

# Max number of octets the RFM69 FIFO can hold
"RFM69_FIFO_SIZE" : 64,

"RFM69_MODE_SLEEP" :    0x00, # 0.1uA
"RFM69_MODE_STDBY" :    0x04, # 1.25mA
"RFM69_MODE_RX" :       0x10, # 16mA
"RFM69_MODE_TX" :       0x0c, # >33mA


# These values we set for FIFO thresholds are actually the same as the POR values
"RF22_TXFFAEM_THRESHOLD" : 4,
"RF22_RXFFAFULL_THRESHOLD" : 55,


# Register names

"RFM69_REG_00_FIFO" :           0x00,
"RFM69_REG_01_OPMODE" :         0x01,
"RFM69_REG_02_DATA_MODUL" :     0x02,
"RFM69_REG_03_BITRATE_MSB" :    0x03,
"RFM69_REG_04_BITRATE_LSB" :    0x04,
"RFM69_REG_05_FDEV_MSB" :       0x05,
"RFM69_REG_06_FDEV_LSB" :       0x06,
"RFM69_REG_07_FRF_MSB" :        0x07,
"RFM69_REG_08_FRF_MID" :        0x08,
"RFM69_REG_09_FRF_LSB" :        0x09,
"RFM69_REG_0A_OSC1" :           0x0A,
"RFM69_REG_0B_AFC_CTRL" :       0x0B,
"RFM69_REG_0D_LISTEN1" :        0x0D,
"RFM69_REG_0E_LISTEN2" :        0x0E,
"RFM69_REG_0F_LISTEN3" :        0x0F,
"RFM69_REG_10_VERSION" :        0x10, #Version and serial number
"RFM69_REG_11_PA_LEVEL" :       0x11,
"RFM69_REG_12_PA_RAMP" :        0x12,
"RFM69_REG_13_OCP" :            0x13,
"RFM69_REG_18_LNA" :            0x18,
"RFM69_REG_19_RX_BW" :          0x19,
"RFM69_REG_1A_AFC_BW" :         0x1A,
"RFM69_REG_1B_OOK_PEAK" :       0x1B,
"RFM69_REG_1C_OOK_AVG" :        0x1C,
"RFM69_REG_1D_OOF_FIX" :        0x1D,
"RFM69_REG_1E_AFC_FEI" :        0x1E,
"RFM69_REG_1F_AFC_MSB" :        0x1F,
"RFM69_REG_20_AFC_LSB" :        0x20,
"RFM69_REG_21_FEI_MSB" :        0x21,
"RFM69_REG_22_FEI_LSB" :        0x22,
"RFM69_REG_23_RSSI_CONFIG" :    0x23,
"RFM69_REG_24_RSSI_VALUE" :     0x24,
"RFM69_REG_25_DIO_MAPPING1" :   0x25,
"RFM69_REG_26_DIO_MAPPING2" :   0x26,
"RFM69_REG_27_IRQ_FLAGS1" :     0x27,
"RFM69_REG_28_IRQ_FLAGS2" :     0x28,
"RFM69_REG_29_RSSI_THRESHOLD" : 0x29,
"RFM69_REG_2A_RX_TIMEOUT1" :    0x2A,
"RFM69_REG_2B_RX_TIMEOUT2" :    0x2B,
"RFM69_REG_2C_PREAMBLE_MSB" :   0x2C,
"RFM69_REG_2D_PREAMBLE_LSB" :   0x2D,
"RFM69_REG_2E_SYNC_CONFIG" :    0x2E,
"RFM69_REG_2F_SYNCVALUE1" :     0x2F,
"RFM69_REG_30_SYNCVALUE2" :     0x30,
# Sync values 1-8 go here
"RFM69_REG_37_PACKET_CONFIG1" : 0x37,
"RFM69_REG_38_PAYLOAD_LENGTH" : 0x38,
# Node address, broadcast address go here
"RFM69_REG_3B_AUTOMODES" :      0x3B,
"RFM69_REG_3C_FIFO_THRESHOLD" : 0x3C,
"RFM69_REG_3D_PACKET_CONFIG2" : 0x3D,
# AES Key 1-16 go here
"RFM69_REG_4E_TEMP1" :          0x4E,
"RFM69_REG_4F_TEMP2" :          0x4F,
"RFM69_REG_58_TEST_LNA" :       0x58,
"RFM69_REG_5A_TEST_PA1" :       0x5A,
"RFM69_REG_5C_TEST_PA2" :       0x5C,
"RFM69_REG_6F_TEST_DAGC" :      0x6F,
"RFM69_REG_71_TEST_AFC" :       0x71,

#******************************************************
# RF69/SX1231 bit control definition
#******************************************************
# RegOpMode
"RF_OPMODE_SEQUENCER_OFF" :             0x80,
"RF_OPMODE_SEQUENCER_ON" :              0x00,  # Default

"RF_OPMODE_LISTEN_ON" :                     0x40,
"RF_OPMODE_LISTEN_OFF" :                    0x00,  # Default

"RF_OPMODE_LISTENABORT" :                   0x20,

"RF_OPMODE_SLEEP" :                         0x00,
"RF_OPMODE_STANDBY" :                       0x04,  # Default
"RF_OPMODE_SYNTHESIZER" :                   0x08,
"RF_OPMODE_TRANSMITTER" :                   0x0C,
"RF_OPMODE_RECEIVER" :                      0x10,

# RegDataModul
"RF_DATAMODUL_DATAMODE_PACKET" :             0x00,  # Default
"RF_DATAMODUL_DATAMODE_CONTINUOUS" :         0x40,
"RF_DATAMODUL_DATAMODE_CONTINUOUSNOBSYNC" :  0x60,

"RF_DATAMODUL_MODULATIONTYPE_FSK" :             0x00,  # Default
"RF_DATAMODUL_MODULATIONTYPE_OOK" :             0x08,

"RF_DATAMODUL_MODULATIONSHAPING_00" :           0x00,  # Default
"RF_DATAMODUL_MODULATIONSHAPING_01" :           0x01,
"RF_DATAMODUL_MODULATIONSHAPING_10" :           0x02,
"RF_DATAMODUL_MODULATIONSHAPING_11" :           0x03,

# RegOsc1
"RF_OSC1_RCCAL_START" :             0x80,
"RF_OSC1_RCCAL_DONE" :              0x40,

# RegAfcCtrl
"RF_AFCLOWBETA_ON" :                    0x20,
"RF_AFCLOWBETA_OFF" :                   0x00,    # Default

# RegLowBat
"RF_LOWBAT_MONITOR" :                   0x10,
"RF_LOWBAT_ON" :                            0x08,
"RF_LOWBAT_OFF" :                           0x00,  # Default

"RF_LOWBAT_TRIM_1695" :             0x00,
"RF_LOWBAT_TRIM_1764" :             0x01,
"RF_LOWBAT_TRIM_1835" :             0x02,  # Default
"RF_LOWBAT_TRIM_1905" :             0x03,
"RF_LOWBAT_TRIM_1976" :             0x04,
"RF_LOWBAT_TRIM_2045" :             0x05,
"RF_LOWBAT_TRIM_2116" :             0x06,
"RF_LOWBAT_TRIM_2185" :             0x07,


# RegListen1
"RF_LISTEN1_RESOL_64" :             0x50,
"RF_LISTEN1_RESOL_4100" :           0xA0,  # Default
"RF_LISTEN1_RESOL_262000" :     	0xF0,

"RF_LISTEN1_CRITERIA_RSSI" :          0x00,  # Default
"RF_LISTEN1_CRITERIA_RSSIANDSYNC" :   0x08,

"RF_LISTEN1_END_00" :                             0x00,
"RF_LISTEN1_END_01" :                             0x02,  # Default
"RF_LISTEN1_END_10" :                             0x04,


# RegListen2
"RF_LISTEN2_COEFIDLE_VALUE" :               0xF5, # Default

# RegListen3
"RF_LISTEN3_COEFRX_VALUE" :                 0x20, # Default

# RegPaLevel
"RF_PALEVEL_PA0_ON" :       0x80,  # Default
"RF_PALEVEL_PA0_OFF" :      0x00,
"RF_PALEVEL_PA1_ON" :       0x40,
"RF_PALEVEL_PA1_OFF" :      0x00,  # Default
"RF_PALEVEL_PA2_ON" :       0x20,
"RF_PALEVEL_PA2_OFF" :      0x00,  # Default


# RegPaRamp
"RF_PARAMP_3400" :                      0x00,
"RF_PARAMP_2000" :                      0x01,
"RF_PARAMP_1000" :                      0x02,
"RF_PARAMP_500" :                       0x03,
"RF_PARAMP_250" :                           0x04,
"RF_PARAMP_125" :                           0x05,
"RF_PARAMP_100" :                           0x06,
"RF_PARAMP_62" :                            0x07,
"RF_PARAMP_50" :                            0x08,
"RF_PARAMP_40" :                            0x09, # Default
"RF_PARAMP_31" :                            0x0A,
"RF_PARAMP_25" :                            0x0B,
"RF_PARAMP_20" :                            0x0C,
"RF_PARAMP_15" :                            0x0D,
"RF_PARAMP_12" :                            0x0E,
"RF_PARAMP_10" :                            0x0F,


# RegOcp
"RF_OCP_OFF" :                              0x0F,
"RF_OCP_ON" :                               0x1A,  # Default

"RF_OCP_TRIM_45" :                      0x00,
"RF_OCP_TRIM_50" :                      0x01,
"RF_OCP_TRIM_55" :                      0x02,
"RF_OCP_TRIM_60" :                      0x03,
"RF_OCP_TRIM_65" :                      0x04,
"RF_OCP_TRIM_70" :                      0x05,
"RF_OCP_TRIM_75" :                      0x06,
"RF_OCP_TRIM_80" :                      0x07,
"RF_OCP_TRIM_85" :                      0x08,
"RF_OCP_TRIM_90" :                      0x09,
"RF_OCP_TRIM_95" :                      0x0A,
"RF_OCP_TRIM_100" :                     0x0B, # Default
"RF_OCP_TRIM_105" :                     0x0C,
"RF_OCP_TRIM_110" :                     0x0D,
"RF_OCP_TRIM_115" :                     0x0E,
"RF_OCP_TRIM_120" :                     0x0F,


# RegAgcRef
"RF_AGCREF_AUTO_ON" :               0x40,  # Default
"RF_AGCREF_AUTO_OFF" :              0x00,

"RF_AGCREF_LEVEL_MINUS80" :     0x00,  # Default
"RF_AGCREF_LEVEL_MINUS81" :     0x01,
"RF_AGCREF_LEVEL_MINUS82" :     0x02,
"RF_AGCREF_LEVEL_MINUS83" :     0x03,
"RF_AGCREF_LEVEL_MINUS84" :     0x04,
"RF_AGCREF_LEVEL_MINUS85" :     0x05,
"RF_AGCREF_LEVEL_MINUS86" :     0x06,
"RF_AGCREF_LEVEL_MINUS87" :     0x07,
"RF_AGCREF_LEVEL_MINUS88" :     0x08,
"RF_AGCREF_LEVEL_MINUS89" :     0x09,
"RF_AGCREF_LEVEL_MINUS90" :     0x0A,
"RF_AGCREF_LEVEL_MINUS91" :     0x0B,
"RF_AGCREF_LEVEL_MINUS92" :     0x0C,
"RF_AGCREF_LEVEL_MINUS93" :     0x0D,
"RF_AGCREF_LEVEL_MINUS94" :     0x0E,
"RF_AGCREF_LEVEL_MINUS95" :     0x0F,
"RF_AGCREF_LEVEL_MINUS96" :     0x10,
"RF_AGCREF_LEVEL_MINUS97" :     0x11,
"RF_AGCREF_LEVEL_MINUS98" :     0x12,
"RF_AGCREF_LEVEL_MINUS99" :     0x13,
"RF_AGCREF_LEVEL_MINUS100" :    0x14,
"RF_AGCREF_LEVEL_MINUS101" :    0x15,
"RF_AGCREF_LEVEL_MINUS102" :    0x16,
"RF_AGCREF_LEVEL_MINUS103" :    0x17,
"RF_AGCREF_LEVEL_MINUS104" :    0x18,
"RF_AGCREF_LEVEL_MINUS105" :    0x19,
"RF_AGCREF_LEVEL_MINUS106" :    0x1A,
"RF_AGCREF_LEVEL_MINUS107" :    0x1B,
"RF_AGCREF_LEVEL_MINUS108" :    0x1C,
"RF_AGCREF_LEVEL_MINUS109" :    0x1D,
"RF_AGCREF_LEVEL_MINUS110" :    0x1E,
"RF_AGCREF_LEVEL_MINUS111" :    0x1F,
"RF_AGCREF_LEVEL_MINUS112" :    0x20,
"RF_AGCREF_LEVEL_MINUS113" :    0x21,
"RF_AGCREF_LEVEL_MINUS114" :    0x22,
"RF_AGCREF_LEVEL_MINUS115" :    0x23,
"RF_AGCREF_LEVEL_MINUS116" :    0x24,
"RF_AGCREF_LEVEL_MINUS117" :    0x25,
"RF_AGCREF_LEVEL_MINUS118" :    0x26,
"RF_AGCREF_LEVEL_MINUS119" :    0x27,
"RF_AGCREF_LEVEL_MINUS120" :    0x28,
"RF_AGCREF_LEVEL_MINUS121" :    0x29,
"RF_AGCREF_LEVEL_MINUS122" :    0x2A,
"RF_AGCREF_LEVEL_MINUS123" :    0x2B,
"RF_AGCREF_LEVEL_MINUS124" :    0x2C,
"RF_AGCREF_LEVEL_MINUS125" :    0x2D,
"RF_AGCREF_LEVEL_MINUS126" :    0x2E,
"RF_AGCREF_LEVEL_MINUS127" :    0x2F,
"RF_AGCREF_LEVEL_MINUS128" :    0x30,
"RF_AGCREF_LEVEL_MINUS129" :    0x31,
"RF_AGCREF_LEVEL_MINUS130" :    0x32,
"RF_AGCREF_LEVEL_MINUS131" :    0x33,
"RF_AGCREF_LEVEL_MINUS132" :    0x34,
"RF_AGCREF_LEVEL_MINUS133" :    0x35,
"RF_AGCREF_LEVEL_MINUS134" :    0x36,
"RF_AGCREF_LEVEL_MINUS135" :    0x37,
"RF_AGCREF_LEVEL_MINUS136" :    0x38,
"RF_AGCREF_LEVEL_MINUS137" :    0x39,
"RF_AGCREF_LEVEL_MINUS138" :    0x3A,
"RF_AGCREF_LEVEL_MINUS139" :    0x3B,
"RF_AGCREF_LEVEL_MINUS140" :    0x3C,
"RF_AGCREF_LEVEL_MINUS141" :    0x3D,
"RF_AGCREF_LEVEL_MINUS142" :    0x3E,
"RF_AGCREF_LEVEL_MINUS143" :    0x3F,


# RegAgcThresh1
"RF_AGCTHRESH1_SNRMARGIN_000" :     0x00,
"RF_AGCTHRESH1_SNRMARGIN_001" :     0x20,
"RF_AGCTHRESH1_SNRMARGIN_010" :     0x40,
"RF_AGCTHRESH1_SNRMARGIN_011" :     0x60,
"RF_AGCTHRESH1_SNRMARGIN_100" :     0x80,
"RF_AGCTHRESH1_SNRMARGIN_101" :     0xA0,  # Default
"RF_AGCTHRESH1_SNRMARGIN_110" :     0xC0,
"RF_AGCTHRESH1_SNRMARGIN_111" :     0xE0,

"RF_AGCTHRESH1_STEP1_0" :                   0x00,
"RF_AGCTHRESH1_STEP1_1" :                   0x01,
"RF_AGCTHRESH1_STEP1_2" :                   0x02,
"RF_AGCTHRESH1_STEP1_3" :                   0x03,
"RF_AGCTHRESH1_STEP1_4" :                   0x04,
"RF_AGCTHRESH1_STEP1_5" :                   0x05,
"RF_AGCTHRESH1_STEP1_6" :                   0x06,
"RF_AGCTHRESH1_STEP1_7" :                   0x07,
"RF_AGCTHRESH1_STEP1_8" :                   0x08,
"RF_AGCTHRESH1_STEP1_9" :                   0x09,
"RF_AGCTHRESH1_STEP1_10" :              0x0A,
"RF_AGCTHRESH1_STEP1_11" :              0x0B,
"RF_AGCTHRESH1_STEP1_12" :              0x0C,
"RF_AGCTHRESH1_STEP1_13" :              0x0D,
"RF_AGCTHRESH1_STEP1_14" :              0x0E,
"RF_AGCTHRESH1_STEP1_15" :              0x0F,
"RF_AGCTHRESH1_STEP1_16" :              0x10,  # Default
"RF_AGCTHRESH1_STEP1_17" :              0x11,
"RF_AGCTHRESH1_STEP1_18" :              0x12,
"RF_AGCTHRESH1_STEP1_19" :              0x13,
"RF_AGCTHRESH1_STEP1_20" :              0x14,
"RF_AGCTHRESH1_STEP1_21" :              0x15,
"RF_AGCTHRESH1_STEP1_22" :              0x16,
"RF_AGCTHRESH1_STEP1_23" :              0x17,
"RF_AGCTHRESH1_STEP1_24" :              0x18,
"RF_AGCTHRESH1_STEP1_25" :              0x19,
"RF_AGCTHRESH1_STEP1_26" :              0x1A,
"RF_AGCTHRESH1_STEP1_27" :              0x1B,
"RF_AGCTHRESH1_STEP1_28" :              0x1C,
"RF_AGCTHRESH1_STEP1_29" :              0x1D,
"RF_AGCTHRESH1_STEP1_30" :              0x1E,
"RF_AGCTHRESH1_STEP1_31" :              0x1F,


# RegAgcThresh2
"RF_AGCTHRESH2_STEP2_0" :                   0x00,
"RF_AGCTHRESH2_STEP2_1" :                   0x10,
"RF_AGCTHRESH2_STEP2_2" :                   0x20,
"RF_AGCTHRESH2_STEP2_3" :                   0x30, # XXX wrong -- Default
"RF_AGCTHRESH2_STEP2_4" :                   0x40,
"RF_AGCTHRESH2_STEP2_5" :                   0x50,
"RF_AGCTHRESH2_STEP2_6" :                   0x60,
"RF_AGCTHRESH2_STEP2_7" :                   0x70,    # default
"RF_AGCTHRESH2_STEP2_8" :                   0x80,
"RF_AGCTHRESH2_STEP2_9" :                   0x90,
"RF_AGCTHRESH2_STEP2_10" :              0xA0,
"RF_AGCTHRESH2_STEP2_11" :              0xB0,
"RF_AGCTHRESH2_STEP2_12" :              0xC0,
"RF_AGCTHRESH2_STEP2_13" :              0xD0,
"RF_AGCTHRESH2_STEP2_14" :              0xE0,
"RF_AGCTHRESH2_STEP2_15" :              0xF0,

"RF_AGCTHRESH2_STEP3_0" :                   0x00,
"RF_AGCTHRESH2_STEP3_1" :                   0x01,
"RF_AGCTHRESH2_STEP3_2" :                   0x02,
"RF_AGCTHRESH2_STEP3_3" :                   0x03,
"RF_AGCTHRESH2_STEP3_4" :                   0x04,
"RF_AGCTHRESH2_STEP3_5" :                   0x05,
"RF_AGCTHRESH2_STEP3_6" :                   0x06,
"RF_AGCTHRESH2_STEP3_7" :                   0x07,
"RF_AGCTHRESH2_STEP3_8" :                   0x08,
"RF_AGCTHRESH2_STEP3_9" :                   0x09,
"RF_AGCTHRESH2_STEP3_10" :              0x0A,
"RF_AGCTHRESH2_STEP3_11" :              0x0B,  # Default
"RF_AGCTHRESH2_STEP3_12" :              0x0C,
"RF_AGCTHRESH2_STEP3_13" :              0x0D,
"RF_AGCTHRESH2_STEP3_14" :              0x0E,
"RF_AGCTHRESH2_STEP3_15" :              0x0F,


# RegAgcThresh3
"RF_AGCTHRESH3_STEP4_0" :                   0x00,
"RF_AGCTHRESH3_STEP4_1" :                   0x10,
"RF_AGCTHRESH3_STEP4_2" :                   0x20,
"RF_AGCTHRESH3_STEP4_3" :                   0x30,
"RF_AGCTHRESH3_STEP4_4" :                   0x40,
"RF_AGCTHRESH3_STEP4_5" :                   0x50,
"RF_AGCTHRESH3_STEP4_6" :                   0x60,
"RF_AGCTHRESH3_STEP4_7" :                   0x70,
"RF_AGCTHRESH3_STEP4_8" :                   0x80,
"RF_AGCTHRESH3_STEP4_9" :                   0x90,  # Default
"RF_AGCTHRESH3_STEP4_10" :              0xA0,
"RF_AGCTHRESH3_STEP4_11" :              0xB0,
"RF_AGCTHRESH3_STEP4_12" :              0xC0,
"RF_AGCTHRESH3_STEP4_13" :              0xD0,
"RF_AGCTHRESH3_STEP4_14" :              0xE0,
"RF_AGCTHRESH3_STEP4_15" :              0xF0,

"RF_AGCTHRESH3_STEP5_0" :                   0x00,
"RF_AGCTHRESH3_STEP5_1" :                   0x01,
"RF_AGCTHRESH3_STEP5_2" :                   0x02,
"RF_AGCTHRESH3_STEP5_3" :                   0x03,
"RF_AGCTHRESH3_STEP5_4" :                   0x04,
"RF_AGCTHRESH3_STEP5_5" :                   0x05,
"RF_AGCTHRESH3_STEP5_6" :                   0x06,
"RF_AGCTHRESH3_STEP5_7" :                   0x07,
"RF_AGCTHRES33_STEP5_8" :                   0x08,
"RF_AGCTHRESH3_STEP5_9" :                   0x09,
"RF_AGCTHRESH3_STEP5_10" :              0x0A,
"RF_AGCTHRESH3_STEP5_11" :              0x0B,  # Default
"RF_AGCTHRESH3_STEP5_12" :              0x0C,
"RF_AGCTHRESH3_STEP5_13" :              0x0D,
"RF_AGCTHRESH3_STEP5_14" :              0x0E,
"RF_AGCTHRESH3_STEP5_15" :              0x0F,


# RegLna
"RF_LNA_ZIN_50" :                               0x00,
"RF_LNA_ZIN_200" :                            0x80,  # Default

"RF_LNA_LOWPOWER_OFF" :                     0x00,  # Default
"RF_LNA_LOWPOWER_ON" :                      0x40,

"RF_LNA_CURRENTGAIN" :                      0x38,

"RF_LNA_GAINSELECT_AUTO" :              0x00,  # Default
"RF_LNA_GAINSELECT_MAX" :                   0x01,
"RF_LNA_GAINSELECT_MAXMINUS6" :     0x02,
"RF_LNA_GAINSELECT_MAXMINUS12" :    0x03,
"RF_LNA_GAINSELECT_MAXMINUS24" :    0x04,
"RF_LNA_GAINSELECT_MAXMINUS36" :    0x05,
"RF_LNA_GAINSELECT_MAXMINUS48" :    0x06,


# RegRxBw
"RF_RXBW_DCCFREQ_000" :                     0x00,
"RF_RXBW_DCCFREQ_001" :                     0x20,
"RF_RXBW_DCCFREQ_010" :                     0x40,  # Default
"RF_RXBW_DCCFREQ_011" :                     0x60,
"RF_RXBW_DCCFREQ_100" :                     0x80,
"RF_RXBW_DCCFREQ_101" :                     0xA0,
"RF_RXBW_DCCFREQ_110" :                     0xC0,
"RF_RXBW_DCCFREQ_111" :                     0xE0,

"RF_RXBW_MANT_16" :                           0x00,
"RF_RXBW_MANT_20" :                           0x08,
"RF_RXBW_MANT_24" :                           0x10,  # Default

"RF_RXBW_EXP_0" :                               0x00,
"RF_RXBW_EXP_1" :                           0x01,
"RF_RXBW_EXP_2" :                           0x02,
"RF_RXBW_EXP_3" :                               0x03,
"RF_RXBW_EXP_4" :                           0x04,
"RF_RXBW_EXP_5" :                           0x05,  # Default
"RF_RXBW_EXP_6" :                             0x06,
"RF_RXBW_EXP_7" :                             0x07,


# RegAfcBw
"RF_AFCBW_DCCFREQAFC_000" :             0x00,
"RF_AFCBW_DCCFREQAFC_001" :             0x20,
"RF_AFCBW_DCCFREQAFC_010" :             0x40,
"RF_AFCBW_DCCFREQAFC_011" :             0x60,
"RF_AFCBW_DCCFREQAFC_100" :             0x80, # Default
"RF_AFCBW_DCCFREQAFC_101" :             0xA0,
"RF_AFCBW_DCCFREQAFC_110" :             0xC0,
"RF_AFCBW_DCCFREQAFC_111" :             0xE0,

"RF_AFCBW_MANTAFC_16" :                     0x00,
"RF_AFCBW_MANTAFC_20" :                     0x08,  # Default
"RF_AFCBW_MANTAFC_24" :                     0x10,

"RF_AFCBW_EXPAFC_0" :                       0x00,
"RF_AFCBW_EXPAFC_1" :                       0x01,
"RF_AFCBW_EXPAFC_2" :                       0x02,
"RF_AFCBW_EXPAFC_3" :                       0x03,  # Default
"RF_AFCBW_EXPAFC_4" :                       0x04,
"RF_AFCBW_EXPAFC_5" :                       0x05,
"RF_AFCBW_EXPAFC_6" :                       0x06,
"RF_AFCBW_EXPAFC_7" :                       0x07,


# RegOokPeak
"RF_OOKPEAK_THRESHTYPE_FIXED" :             0x00,
"RF_OOKPEAK_THRESHTYPE_PEAK" :              0x40,  # Default
"RF_OOKPEAK_THRESHTYPE_AVERAGE" :           0x80,

"RF_OOKPEAK_PEAKTHRESHSTEP_000" :           0x00,  # Default
"RF_OOKPEAK_PEAKTHRESHSTEP_001" :           0x08,
"RF_OOKPEAK_PEAKTHRESHSTEP_010" :           0x10,
"RF_OOKPEAK_PEAKTHRESHSTEP_011" :           0x18,
"RF_OOKPEAK_PEAKTHRESHSTEP_100" :           0x20,
"RF_OOKPEAK_PEAKTHRESHSTEP_101" :           0x28,
"RF_OOKPEAK_PEAKTHRESHSTEP_110" :           0x30,
"RF_OOKPEAK_PEAKTHRESHSTEP_111" :           0x38,

"RF_OOKPEAK_PEAKTHRESHDEC_000" :            0x00,  # Default
"RF_OOKPEAK_PEAKTHRESHDEC_001" :            0x01,
"RF_OOKPEAK_PEAKTHRESHDEC_010" :            0x02,
"RF_OOKPEAK_PEAKTHRESHDEC_011" :            0x03,
"RF_OOKPEAK_PEAKTHRESHDEC_100" :            0x04,
"RF_OOKPEAK_PEAKTHRESHDEC_101" :            0x05,
"RF_OOKPEAK_PEAKTHRESHDEC_110" :            0x06,
"RF_OOKPEAK_PEAKTHRESHDEC_111" :            0x07,


# RegOokAvg
"RF_OOKAVG_AVERAGETHRESHFILT_00" :      0x00,
"RF_OOKAVG_AVERAGETHRESHFILT_01" :      0x40,
"RF_OOKAVG_AVERAGETHRESHFILT_10" :      0x80,  # Default
"RF_OOKAVG_AVERAGETHRESHFILT_11" :      0xC0,


# RegOokFix
"RF_OOKFIX_FIXEDTHRESH_VALUE" :             0x06,  # Default


# RegAfcFei
"RF_AFCFEI_FEI_DONE" :                          0x40,
"RF_AFCFEI_FEI_START" :                         0x20,
"RF_AFCFEI_AFC_DONE" :                          0x10,
"RF_AFCFEI_AFCAUTOCLEAR_ON" :               0x08,
"RF_AFCFEI_AFCAUTOCLEAR_OFF" :              0x00,  # Default

"RF_AFCFEI_AFCAUTO_ON" :                        0x04,
"RF_AFCFEI_AFCAUTO_OFF" :                       0x00,  # Default

"RF_AFCFEI_AFC_CLEAR" :                         0x02,
"RF_AFCFEI_AFC_START" :                         0x01,

# RegRssiConfig
"RF_RSSI_FASTRX_ON" :                             0x08,
"RF_RSSI_FASTRX_OFF" :                          0x00,  # Default
"RF_RSSI_DONE" :                                    0x02,
"RF_RSSI_START" :                                   0x01,


# RegDioMapping1
"RF_DIOMAPPING1_DIO0_00" :                  0x00,  # Default
"RF_DIOMAPPING1_DIO0_01" :                  0x40,
"RF_DIOMAPPING1_DIO0_10" :                  0x80,
"RF_DIOMAPPING1_DIO0_11" :                  0xC0,

"RF_DIOMAPPING1_DIO1_00" :                      0x00,  # Default
"RF_DIOMAPPING1_DIO1_01" :                  0x10,
"RF_DIOMAPPING1_DIO1_10" :                  0x20,
"RF_DIOMAPPING1_DIO1_11" :                  0x30,

"RF_DIOMAPPING1_DIO2_00" :                  0x00,  # Default
"RF_DIOMAPPING1_DIO2_01" :                  0x04,
"RF_DIOMAPPING1_DIO2_10" :                  0x08,
"RF_DIOMAPPING1_DIO2_11" :                  0x0C,

"RF_DIOMAPPING1_DIO3_00" :                  0x00,  # Default
"RF_DIOMAPPING1_DIO3_01" :                  0x01,
"RF_DIOMAPPING1_DIO3_10" :                  0x02,
"RF_DIOMAPPING1_DIO3_11" :                  0x03,


# RegDioMapping2
"RF_DIOMAPPING2_DIO4_00" :                  0x00,  # Default
"RF_DIOMAPPING2_DIO4_01" :                  0x40,
"RF_DIOMAPPING2_DIO4_10" :                  0x80,
"RF_DIOMAPPING2_DIO4_11" :                  0xC0,

"RF_DIOMAPPING2_DIO5_00" :                  0x00,  # Default
"RF_DIOMAPPING2_DIO5_01" :                  0x10,
"RF_DIOMAPPING2_DIO5_10" :                  0x20,
"RF_DIOMAPPING2_DIO5_11" :                  0x30,

"RF_DIOMAPPING2_CLKOUT_32" :                0x00,
"RF_DIOMAPPING2_CLKOUT_16" :                0x01,
"RF_DIOMAPPING2_CLKOUT_8" :                 0x02,
"RF_DIOMAPPING2_CLKOUT_4" :                   0x03,
"RF_DIOMAPPING2_CLKOUT_2" :                 0x04,
"RF_DIOMAPPING2_CLKOUT_1" :                 0x05,
"RF_DIOMAPPING2_CLKOUT_RC" :                0x06,
"RF_DIOMAPPING2_CLKOUT_OFF" :                 0x07,  # Default


# RegIrqFlags1
"RF_IRQFLAGS1_MODEREADY" :                    0x80,
"RF_IRQFLAGS1_RXREADY" :                        0x40,
"RF_IRQFLAGS1_TXREADY" :                        0x20,
"RF_IRQFLAGS1_PLLLOCK" :                        0x10,
"RF_IRQFLAGS1_RSSI" :                             0x08,
"RF_IRQFLAGS1_TIMEOUT" :                        0x04,
"RF_IRQFLAGS1_AUTOMODE" :                       0x02,
"RF_IRQFLAGS1_SYNCADDRESSMATCH" :           0x01,

# RegIrqFlags2
"RF_IRQFLAGS2_FIFOFULL" :                       0x80,
"RF_IRQFLAGS2_FIFONOTEMPTY" :                 0x40,
"RF_IRQFLAGS2_FIFOLEVEL" :                    0x20,
"RF_IRQFLAGS2_FIFOOVERRUN" :                  0x10,
"RF_IRQFLAGS2_PACKETSENT" :                   0x08,
"RF_IRQFLAGS2_PAYLOADREADY" :                0x04,
"RF_IRQFLAGS2_CRCOK" :                          0x02,
"RF_IRQFLAGS2_LOWBAT" :                         0x01,

# RegRssiThresh
"RF_RSSITHRESH_VALUE" :                         0xE4,  # Default

# RegRxTimeout1
"RF_RXTIMEOUT1_RXSTART_VALUE" :             0x00,  # Default

# RegRxTimeout2
"RF_RXTIMEOUT2_RSSITHRESH_VALUE" :      0x00,  # Default

# RegPreamble
"RF_PREAMBLESIZE_MSB_VALUE" :                 0x00,  # Default
"RF_PREAMBLESIZE_LSB_VALUE" :                 0x03,  # Default


# RegSyncConfig
"RF_SYNC_ON" :                              0x80,  # Default
"RF_SYNC_OFF" :                             0x00,

"RF_SYNC_FIFOFILL_AUTO" :           0x00,  # Default -- when sync interrupt occurs
"RF_SYNC_FIFOFILL_MANUAL" :     0x40,

"RF_SYNC_SIZE_1" :                      0x00,
"RF_SYNC_SIZE_2" :                      0x08,
"RF_SYNC_SIZE_3" :                      0x10,
"RF_SYNC_SIZE_4" :                      0x18, # Default
"RF_SYNC_SIZE_5" :                      0x20,
"RF_SYNC_SIZE_6" :                      0x28,
"RF_SYNC_SIZE_7" :                      0x30,
"RF_SYNC_SIZE_8" :                      0x38,

"RF_SYNC_TOL_0" :                           0x00,  # Default
"RF_SYNC_TOL_1" :                           0x01,
"RF_SYNC_TOL_2" :                           0x02,
"RF_SYNC_TOL_3" :                           0x03,
"RF_SYNC_TOL_4" :                           0x04,
"RF_SYNC_TOL_5" :                           0x05,
"RF_SYNC_TOL_6" :                           0x06,
"RF_SYNC_TOL_7" :                           0x07,


# RegSyncValue1-8
"RF_SYNC_BYTE1_VALUE" :             0x00,  # Default
"RF_SYNC_BYTE2_VALUE" :             0x00,  # Default
"RF_SYNC_BYTE3_VALUE" :             0x00,  # Default
"RF_SYNC_BYTE4_VALUE" :             0x00,  # Default
"RF_SYNC_BYTE5_VALUE" :             0x00,  # Default
"RF_SYNC_BYTE6_VALUE" :             0x00,  # Default
"RF_SYNC_BYTE7_VALUE" :             0x00,  # Default
"RF_SYNC_BYTE8_VALUE" :             0x00,  # Default


# RegPacketConfig1
"RF_PACKET1_FORMAT_FIXED" :         0x00,  # Default
"RF_PACKET1_FORMAT_VARIABLE" :      0x80,

"RF_PACKET1_DCFREE_OFF" :           0x00,  # Default
"RF_PACKET1_DCFREE_MANCHESTER" :    0x20,
"RF_PACKET1_DCFREE_WHITENING" :     0x40,

"RF_PACKET1_CRC_ON" :                         0x10,  # Default
"RF_PACKET1_CRC_OFF" :                      0x00,

"RF_PACKET1_CRCAUTOCLEAR_ON" :      0x00,  # Default
"RF_PACKET1_CRCAUTOCLEAR_OFF" :     0x08,

"RF_PACKET1_ADRSFILTERING_OFF" :                  0x00,  # Default
"RF_PACKET1_ADRSFILTERING_NODE" :                 0x02,
"RF_PACKET1_ADRSFILTERING_NODEBROADCAST" :  0x04,


# RegPayloadLength
"RF_PAYLOADLENGTH_VALUE" :                  0x40,  # Default

# RegBroadcastAdrs
"RF_BROADCASTADDRESS_VALUE" :               0x00,


# RegAutoModes
"RF_AUTOMODES_ENTER_OFF" :                        0x00,  # Default
"RF_AUTOMODES_ENTER_FIFONOTEMPTY" :           0x20,
"RF_AUTOMODES_ENTER_FIFOLEVEL" :                0x40,
"RF_AUTOMODES_ENTER_CRCOK" :                      0x60,
"RF_AUTOMODES_ENTER_PAYLOADREADY" :           0x80,
"RF_AUTOMODES_ENTER_SYNCADRSMATCH" :          0xA0,
"RF_AUTOMODES_ENTER_PACKETSENT" :               0xC0,
"RF_AUTOMODES_ENTER_FIFOEMPTY" :                0xE0,

"RF_AUTOMODES_EXIT_OFF" :                           0x00,  # Default
"RF_AUTOMODES_EXIT_FIFOEMPTY" :              0x04,
"RF_AUTOMODES_EXIT_FIFOLEVEL" :               0x08,
"RF_AUTOMODES_EXIT_CRCOK" :                       0x0C,
"RF_AUTOMODES_EXIT_PAYLOADREADY" :          0x10,
"RF_AUTOMODES_EXIT_SYNCADRSMATCH" :           0x14,
"RF_AUTOMODES_EXIT_PACKETSENT" :              0x18,
"RF_AUTOMODES_EXIT_RXTIMEOUT" :                 0x1C,

"RF_AUTOMODES_INTERMEDIATE_SLEEP" :           0x00,  # Default
"RF_AUTOMODES_INTERMEDIATE_STANDBY" :         0x01,
"RF_AUTOMODES_INTERMEDIATE_RECEIVER" :      0x02,
"RF_AUTOMODES_INTERMEDIATE_TRANSMITTER" :   0x03,


# RegFifoThresh
"RF_FIFOTHRESH_TXSTART_FIFOTHRESH" :          0x00,
"RF_FIFOTHRESH_TXSTART_FIFONOTEMPTY" :      0x80,  # Default

"RF_FIFOTHRESH_VALUE" :                             0x0F,  # Default


# RegPacketConfig2
"RF_PACKET2_RXRESTARTDELAY_1BIT" :            0x00,  # Default
"RF_PACKET2_RXRESTARTDELAY_2BITS" :           0x10,
"RF_PACKET2_RXRESTARTDELAY_4BITS" :         0x20,
"RF_PACKET2_RXRESTARTDELAY_8BITS" :         0x30,
"RF_PACKET2_RXRESTARTDELAY_16BITS" :          0x40,
"RF_PACKET2_RXRESTARTDELAY_32BITS" :        0x50,
"RF_PACKET2_RXRESTARTDELAY_64BITS" :        0x60,
"RF_PACKET2_RXRESTARTDELAY_128BITS" :         0x70,
"RF_PACKET2_RXRESTARTDELAY_256BITS" :       0x80,
"RF_PACKET2_RXRESTARTDELAY_512BITS" :       0x90,
"RF_PACKET2_RXRESTARTDELAY_1024BITS" :      0xA0,
"RF_PACKET2_RXRESTARTDELAY_2048BITS" :      0xB0,
"RF_PACKET2_RXRESTARTDELAY_NONE" :            0xC0,
"RF_PACKET2_RXRESTART" :                            0x04,

"RF_PACKET2_AUTORXRESTART_ON" :                 0x02,  # Default
"RF_PACKET2_AUTORXRESTART_OFF" :                0x00,

"RF_PACKET2_AES_ON" :                                 0x01,
"RF_PACKET2_AES_OFF" :                              0x00,  # Default


# RegAesKey1-16
"RF_AESKEY1_VALUE" :                        0x00,  # Default
"RF_AESKEY2_VALUE" :                        0x00,  # Default
"RF_AESKEY3_VALUE" :                        0x00,  # Default
"RF_AESKEY4_VALUE" :                        0x00,  # Default
"RF_AESKEY5_VALUE" :                        0x00,  # Default
"RF_AESKEY6_VALUE" :                        0x00,  # Default
"RF_AESKEY7_VALUE" :                        0x00,  # Default
"RF_AESKEY8_VALUE" :                        0x00,  # Default
"RF_AESKEY9_VALUE" :                        0x00,  # Default
"RF_AESKEY10_VALUE" :                       0x00,  # Default
"RF_AESKEY11_VALUE" :                      0x00,  # Default
"RF_AESKEY12_VALUE" :                       0x00,  # Default
"RF_AESKEY13_VALUE" :                      0x00,  # Default
"RF_AESKEY14_VALUE" :                       0x00,  # Default
"RF_AESKEY15_VALUE" :                       0x00,  # Default
"RF_AESKEY16_VALUE" :                       0x00,  # Default


# RegTemp1
"RF_TEMP1_MEAS_START" :                0x08,
"RF_TEMP1_MEAS_RUNNING" :               0x04,
"RF_TEMP1_ADCLOWPOWER_ON" :         0x01,  # Default
"RF_TEMP1_ADCLOWPOWER_OFF" :        0x00,

# RegTestDagc
"RF_DAGC_NORMAL" :              0x00,  # Reset value
"RF_DAGC_IMPROVED_LOWBETA1" :   0x20,  #
"RF_DAGC_IMPROVED_LOWBETA0" :   0x30,  # Recommended default

# RegTestLna
"RF_TESTLNA_NORMAL" :           0x1B,  # Default
"RF_TESTLNA_SENSITIVE" :        0x2D  #
}

config = {
    "RFM69_REG_01_OPMODE" :      registers["RF_OPMODE_SEQUENCER_ON"] | registers["RF_OPMODE_LISTEN_OFF"] | registers["RFM69_MODE_RX"],
    "RFM69_REG_02_DATA_MODUL" :  registers["RF_DATAMODUL_DATAMODE_PACKET"] | registers["RF_DATAMODUL_MODULATIONTYPE_FSK"] | registers["RF_DATAMODUL_MODULATIONSHAPING_00"],
    
    "RFM69_REG_03_BITRATE_MSB" : 0x3E, # 2000 bps
    "RFM69_REG_04_BITRATE_LSB" : 0x80,
    
    "RFM69_REG_05_FDEV_MSB" :    0x00, # 12000 hz (24000 hz shift)
    "RFM69_REG_06_FDEV_LSB" :    0xC5,

    "RFM69_REG_07_FRF_MSB" :     0xD9, # 869.5 MHz
    "RFM69_REG_08_FRF_MID" :     0x60, # calculated: 0x80?
    "RFM69_REG_09_FRF_LSB" :     0x12,
    
    "RFM69_REG_0B_AFC_CTRL" :    registers["RF_AFCLOWBETA_OFF"], # AFC Offset On
    
    # PA Settings
    # +20dBm formula: Pout=-11+OutputPower[dBmW] (with PA1 and PA2)** and high power PA settings (section 3.3.7 in datasheet)
    # Without extra flags: Pout=-14+OutputPower[dBmW]
    #[ RFM69_REG_11_PA_LEVEL,    RF_PALEVEL_PA0_OFF | RF_PALEVEL_PA1_ON | RF_PALEVEL_PA2_ON | 0x18],  // 10mW
    "RFM69_REG_11_PA_LEVEL" : registers["RF_PALEVEL_PA0_OFF"] | registers["RF_PALEVEL_PA1_ON"] | registers["RF_PALEVEL_PA2_ON"] | 0x1f, # 50mW
    
    "RFM69_REG_12_PA_RAMP" : registers["RF_PARAMP_500"], # 500us PA ramp-up (1 bit)
    
    "RFM69_REG_13_OCP" :         registers["RF_OCP_ON"] | registers["RF_OCP_TRIM_95"],
    
    "RFM69_REG_18_LNA" :         registers["RF_LNA_ZIN_50"], # 50 ohm for matched antenna, 200 otherwise
    
    "RFM69_REG_19_RX_BW" :       registers["RF_RXBW_DCCFREQ_010"] | registers["RF_RXBW_MANT_16"] | registers["RF_RXBW_EXP_2"], # Rx Bandwidth: 128KHz
    
    "RFM69_REG_1E_AFC_FEI" :     registers["RF_AFCFEI_AFCAUTO_ON"] | registers["RF_AFCFEI_AFCAUTOCLEAR_ON"], # Automatic AFC on, clear after each packet
    
    "RFM69_REG_25_DIO_MAPPING1" : registers["RF_DIOMAPPING1_DIO0_01"],
    "RFM69_REG_26_DIO_MAPPING2" : registers["RF_DIOMAPPING2_CLKOUT_OFF"], # Switch off Clkout
    
    # [ RFM69_REG_2D_PREAMBLE_LSB, RF_PREAMBLESIZE_LSB_VALUE ] # default 3 preamble bytes 0xAAAAAA
    
    #[ RFM69_REG_2E_SYNC_CONFIG, RF_SYNC_OFF | RF_SYNC_FIFOFILL_MANUAL ], # Sync bytes off
    "RFM69_REG_2E_SYNC_CONFIG" : registers["RF_SYNC_ON"] | registers["RF_SYNC_FIFOFILL_AUTO"] | registers["RF_SYNC_SIZE_2"] | registers["RF_SYNC_TOL_0"],
    "RFM69_REG_2F_SYNCVALUE1" : 0x2D,
    "RFM69_REG_30_SYNCVALUE2" : 0xAA,
    "RFM69_REG_37_PACKET_CONFIG1" : registers["RF_PACKET1_FORMAT_VARIABLE"] | registers["RF_PACKET1_DCFREE_OFF"] | registers["RF_PACKET1_CRC_ON"] | registers["RF_PACKET1_CRCAUTOCLEAR_ON"] | registers["RF_PACKET1_ADRSFILTERING_OFF"],
    "RFM69_REG_38_PAYLOAD_LENGTH" : registers["RFM69_FIFO_SIZE"], # Full FIFO size for rx packet
	#[ RFM69_REG_3B_AUTOMODES, RF_AUTOMODES_ENTER_FIFONOTEMPTY | RF_AUTOMODES_EXIT_PACKETSENT | RF_AUTOMODES_INTERMEDIATE_TRANSMITTER ],
    "RFM69_REG_3C_FIFO_THRESHOLD" : registers["RF_FIFOTHRESH_TXSTART_FIFONOTEMPTY"] | 0x05, #TX on FIFO not empty
    "RFM69_REG_3D_PACKET_CONFIG2" : registers["RF_PACKET2_RXRESTARTDELAY_2BITS"] | registers["RF_PACKET2_AUTORXRESTART_ON"] | registers["RF_PACKET2_AES_OFF"], #RXRESTARTDELAY must match transmitter PA ramp-down time (bitrate dependent)
    "RFM69_REG_6F_TEST_DAGC" : registers["RF_DAGC_IMPROVED_LOWBETA0"] # run DAGC continuously in RX mode, recommended default for AfcLowBetaOn=0
	#[ RFM69_REG_71_TEST_AFC, 0x0E ], //14* 488hz = ~7KHz
    #[255, 0]
}
