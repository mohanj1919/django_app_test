# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-21 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0018_auto_20170821_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='code_type',
            field=models.CharField(choices=[('ICD9', 'ICD9 Diagnosis'), ('ICD10', 'ICD10'), ('MEDCIN', 'MEDCIN'), ('SNOMED', 'SNOMED')], max_length=100),
        ),
        migrations.AlterField(
            model_name='encounter',
            name='discharge_disposition',
            field=models.CharField(choices=[('0', ' 0'), ('1', ' 1'), ('2', ' 2'), ('3', ' 3'), ('4', ' 4'), ('5', ' 5'), ('6', ' 6'), ('7', ' 7'), ('8', ' 8'), ('9', ' 9'), ('20', ' 20'), ('21', ' 21'), ('30', ' 30'), ('40', ' 40'), ('41', ' 41'), ('42', ' 42'), ('43', ' 43'), ('50', ' 50'), ('51', ' 51'), ('61', ' 61'), ('62', ' 62'), ('63', ' 63'), ('64', ' 64'), ('65', ' 65'), ('66', ' 66'), ('69', ' 69'), ('70', ' 70'), ('71', ' 71'), ('72', ' 72'), ('81', ' 81'), ('82', ' 82'), ('83', ' 83'), ('84', ' 84'), ('85', ' 85'), ('86', ' 86'), ('87', ' 87'), ('88', ' 88'), ('89', ' 89'), ('90', ' 90'), ('91', ' 91'), ('92', ' 92'), ('93', ' 93'), ('94', ' 94'), ('95', ' 95')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='encounter',
            name='place_of_service',
            field=models.CharField(choices=[('1', ' 1'), ('2', ' 2'), ('3', ' 3'), ('4', ' 4'), ('5', ' 5'), ('6', ' 6'), ('7', ' 7'), ('8', ' 8'), ('9', ' 9'), ('11', ' 11'), ('12', ' 12'), ('13', ' 13'), ('14', ' 14'), ('15', ' 15'), ('16', ' 16'), ('17', ' 17'), ('18', ' 18'), ('19', ' 19'), ('20', ' 20'), ('21', ' 21'), ('22', ' 22'), ('23', ' 23'), ('24', ' 24'), ('25', ' 25'), ('26', ' 26'), ('31', ' 31'), ('32', ' 32'), ('33', ' 33'), ('34', ' 34'), ('41', ' 41'), ('42', ' 42'), ('49', ' 49'), ('50', ' 50'), ('51', ' 51'), ('52', ' 52'), ('53', ' 53'), ('54', ' 54'), ('55', ' 55'), ('56', ' 56'), ('57', ' 57'), ('60', ' 60'), ('61', ' 61'), ('62', ' 62'), ('65', ' 65'), ('71', ' 71'), ('72', ' 72'), ('81', ' 81'), ('99', ' 99')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='encounter',
            name='type_of_bill',
            field=models.CharField(choices=[('110', ' 110'), ('111', ' 111'), ('112', ' 112'), ('113', ' 113'), ('114', ' 114'), ('115', ' 115'), ('116', ' 116'), ('117', ' 117'), ('118', ' 118'), ('119', ' 119'), ('120', ' 120'), ('121', ' 121'), ('122', ' 122'), ('123', ' 123'), ('124', ' 124'), ('125', ' 125'), ('126', ' 126'), ('127', ' 127'), ('128', ' 128'), ('129', ' 129'), ('130', ' 130'), ('131', ' 131'), ('132', ' 132'), ('133', ' 133'), ('134', ' 134'), ('135', ' 135'), ('136', ' 136'), ('137', ' 137'), ('138', ' 138'), ('139', ' 139'), ('140', ' 140'), ('141', ' 141'), ('142', ' 142'), ('143', ' 143'), ('144', ' 144'), ('145', ' 145'), ('146', ' 146'), ('147', ' 147'), ('148', ' 148'), ('149', ' 149'), ('150', ' 150'), ('151', ' 151'), ('152', ' 152'), ('153', ' 153'), ('154', ' 154'), ('155', ' 155'), ('156', ' 156'), ('157', ' 157'), ('158', ' 158'), ('159', ' 159'), ('160', ' 160'), ('161', ' 161'), ('162', ' 162'), ('163', ' 163'), ('164', ' 164'), ('165', ' 165'), ('166', ' 166'), ('167', ' 167'), ('168', ' 168'), ('169', ' 169'), ('170', ' 170'), ('171', ' 171'), ('172', ' 172'), ('173', ' 173'), ('174', ' 174'), ('175', ' 175'), ('176', ' 176'), ('177', ' 177'), ('178', ' 178'), ('179', ' 179'), ('180', ' 180'), ('181', ' 181'), ('182', ' 182'), ('183', ' 183'), ('184', ' 184'), ('185', ' 185'), ('186', ' 186'), ('187', ' 187'), ('188', ' 188'), ('189', ' 189'), ('210', ' 210'), ('211', ' 211'), ('212', ' 212'), ('213', ' 213'), ('214', ' 214'), ('215', ' 215'), ('216', ' 216'), ('217', ' 217'), ('218', ' 218'), ('219', ' 219'), ('220', ' 220'), ('221', ' 221'), ('222', ' 222'), ('223', ' 223'), ('224', ' 224'), ('225', ' 225'), ('226', ' 226'), ('227', ' 227'), ('228', ' 228'), ('229', ' 229'), ('230', ' 230'), ('231', ' 231'), ('232', ' 232'), ('233', ' 233'), ('234', ' 234'), ('235', ' 235'), ('236', ' 236'), ('237', ' 237'), ('238', ' 238'), ('239', ' 239'), ('240', ' 240'), ('241', ' 241'), ('242', ' 242'), ('243', ' 243'), ('244', ' 244'), ('245', ' 245'), ('246', ' 246'), ('247', ' 247'), ('248', ' 248'), ('249', ' 249'), ('250', ' 250'), ('251', ' 251'), ('252', ' 252'), ('253', ' 253'), ('254', ' 254'), ('255', ' 255'), ('256', ' 256'), ('257', ' 257'), ('258', ' 258'), ('259', ' 259'), ('260', ' 260'), ('261', ' 261'), ('262', ' 262'), ('263', ' 263'), ('264', ' 264'), ('265', ' 265'), ('266', ' 266'), ('267', ' 267'), ('268', ' 268'), ('269', ' 269'), ('270', ' 270'), ('271', ' 271'), ('272', ' 272'), ('273', ' 273'), ('274', ' 274'), ('275', ' 275'), ('276', ' 276'), ('277', ' 277'), ('278', ' 278'), ('279', ' 279'), ('280', ' 280'), ('281', ' 281'), ('282', ' 282'), ('283', ' 283'), ('284', ' 284'), ('285', ' 285'), ('286', ' 286'), ('287', ' 287'), ('288', ' 288'), ('289', ' 289'), ('310', ' 310'), ('311', ' 311'), ('312', ' 312'), ('313', ' 313'), ('314', ' 314'), ('315', ' 315'), ('316', ' 316'), ('317', ' 317'), ('318', ' 318'), ('319', ' 319'), ('320', ' 320'), ('321', ' 321'), ('322', ' 322'), ('323', ' 323'), ('324', ' 324'), ('325', ' 325'), ('326', ' 326'), ('327', ' 327'), ('328', ' 328'), ('329', ' 329'), ('330', ' 330'), ('331', ' 331'), ('332', ' 332'), ('333', ' 333'), ('334', ' 334'), ('335', ' 335'), ('336', ' 336'), ('337', ' 337'), ('338', ' 338'), ('339', ' 339'), ('340', ' 340'), ('341', ' 341'), ('342', ' 342'), ('343', ' 343'), ('344', ' 344'), ('345', ' 345'), ('346', ' 346'), ('347', ' 347'), ('348', ' 348'), ('349', ' 349'), ('350', ' 350'), ('351', ' 351'), ('352', ' 352'), ('353', ' 353'), ('354', ' 354'), ('355', ' 355'), ('356', ' 356'), ('357', ' 357'), ('358', ' 358'), ('359', ' 359'), ('360', ' 360'), ('361', ' 361'), ('362', ' 362'), ('363', ' 363'), ('364', ' 364'), ('365', ' 365'), ('366', ' 366'), ('367', ' 367'), ('368', ' 368'), ('369', ' 369'), ('370', ' 370'), ('371', ' 371'), ('372', ' 372'), ('373', ' 373'), ('374', ' 374'), ('375', ' 375'), ('376', ' 376'), ('377', ' 377'), ('378', ' 378'), ('379', ' 379'), ('380', ' 380'), ('381', ' 381'), ('382', ' 382'), ('383', ' 383'), ('384', ' 384'), ('385', ' 385'), ('386', ' 386'), ('387', ' 387'), ('388', ' 388'), ('389', ' 389'), ('410', ' 410'), ('411', ' 411'), ('412', ' 412'), ('413', ' 413'), ('414', ' 414'), ('415', ' 415'), ('416', ' 416'), ('417', ' 417'), ('418', ' 418'), ('419', ' 419'), ('420', ' 420'), ('421', ' 421'), ('422', ' 422'), ('423', ' 423'), ('424', ' 424'), ('425', ' 425'), ('426', ' 426'), ('427', ' 427'), ('428', ' 428'), ('429', ' 429'), ('430', ' 430'), ('431', ' 431'), ('432', ' 432'), ('433', ' 433'), ('434', ' 434'), ('435', ' 435'), ('436', ' 436'), ('437', ' 437'), ('438', ' 438'), ('439', ' 439'), ('440', ' 440'), ('441', ' 441'), ('442', ' 442'), ('443', ' 443'), ('444', ' 444'), ('445', ' 445'), ('446', ' 446'), ('447', ' 447'), ('448', ' 448'), ('449', ' 449'), ('450', ' 450'), ('451', ' 451'), ('452', ' 452'), ('453', ' 453'), ('454', ' 454'), ('455', ' 455'), ('456', ' 456'), ('457', ' 457'), ('458', ' 458'), ('459', ' 459'), ('460', ' 460'), ('461', ' 461'), ('462', ' 462'), ('463', ' 463'), ('464', ' 464'), ('465', ' 465'), ('466', ' 466'), ('467', ' 467'), ('468', ' 468'), ('469', ' 469'), ('470', ' 470'), ('471', ' 471'), ('472', ' 472'), ('473', ' 473'), ('474', ' 474'), ('475', ' 475'), ('476', ' 476'), ('477', ' 477'), ('478', ' 478'), ('479', ' 479'), ('480', ' 480'), ('481', ' 481'), ('482', ' 482'), ('483', ' 483'), ('484', ' 484'), ('485', ' 485'), ('486', ' 486'), ('487', ' 487'), ('488', ' 488'), ('489', ' 489'), ('510', ' 510'), ('511', ' 511'), ('512', ' 512'), ('513', ' 513'), ('514', ' 514'), ('515', ' 515'), ('516', ' 516'), ('517', ' 517'), ('518', ' 518'), ('519', ' 519'), ('520', ' 520'), ('521', ' 521'), ('522', ' 522'), ('523', ' 523'), ('524', ' 524'), ('525', ' 525'), ('526', ' 526'), ('527', ' 527'), ('528', ' 528'), ('529', ' 529'), ('530', ' 530'), ('531', ' 531'), ('532', ' 532'), ('533', ' 533'), ('534', ' 534'), ('535', ' 535'), ('536', ' 536'), ('537', ' 537'), ('538', ' 538'), ('539', ' 539'), ('540', ' 540'), ('541', ' 541'), ('542', ' 542'), ('543', ' 543'), ('544', ' 544'), ('545', ' 545'), ('546', ' 546'), ('547', ' 547'), ('548', ' 548'), ('549', ' 549'), ('550', ' 550'), ('551', ' 551'), ('552', ' 552'), ('553', ' 553'), ('554', ' 554'), ('555', ' 555'), ('556', ' 556'), ('557', ' 557'), ('558', ' 558'), ('559', ' 559'), ('560', ' 560'), ('561', ' 561'), ('562', ' 562'), ('563', ' 563'), ('564', ' 564'), ('565', ' 565'), ('566', ' 566'), ('567', ' 567'), ('568', ' 568'), ('569', ' 569'), ('570', ' 570'), ('571', ' 571'), ('572', ' 572'), ('573', ' 573'), ('574', ' 574'), ('575', ' 575'), ('576', ' 576'), ('577', ' 577'), ('578', ' 578'), ('579', ' 579'), ('580', ' 580'), ('581', ' 581'), ('582', ' 582'), ('583', ' 583'), ('584', ' 584'), ('585', ' 585'), ('586', ' 586'), ('587', ' 587'), ('588', ' 588'), ('589', ' 589'), ('710', ' 710'), ('711', ' 711'), ('712', ' 712'), ('713', ' 713'), ('714', ' 714'), ('715', ' 715'), ('716', ' 716'), ('717', ' 717'), ('718', ' 718'), ('719', ' 719'), ('720', ' 720'), ('721', ' 721'), ('722', ' 722'), ('723', ' 723'), ('724', ' 724'), ('725', ' 725'), ('726', ' 726'), ('727', ' 727'), ('728', ' 728'), ('729', ' 729'), ('730', ' 730'), ('731', ' 731'), ('732', ' 732'), ('733', ' 733'), ('734', ' 734'), ('735', ' 735'), ('736', ' 736'), ('737', ' 737'), ('738', ' 738'), ('739', ' 739'), ('740', ' 740'), ('741', ' 741'), ('742', ' 742'), ('743', ' 743'), ('744', ' 744'), ('745', ' 745'), ('746', ' 746'), ('747', ' 747'), ('748', ' 748'), ('749', ' 749'), ('750', ' 750'), ('751', ' 751'), ('752', ' 752'), ('753', ' 753'), ('754', ' 754'), ('755', ' 755'), ('756', ' 756'), ('757', ' 757'), ('758', ' 758'), ('759', ' 759'), ('760', ' 760'), ('761', ' 761'), ('762', ' 762'), ('763', ' 763'), ('764', ' 764'), ('765', ' 765'), ('766', ' 766'), ('767', ' 767'), ('768', ' 768'), ('769', ' 769'), ('810', ' 810'), ('811', ' 811'), ('812', ' 812'), ('813', ' 813'), ('814', ' 814'), ('815', ' 815'), ('816', ' 816'), ('817', ' 817'), ('818', ' 818'), ('819', ' 819'), ('820', ' 820'), ('821', ' 821'), ('822', ' 822'), ('823', ' 823'), ('824', ' 824'), ('825', ' 825'), ('826', ' 826'), ('827', ' 827'), ('828', ' 828'), ('829', ' 829'), ('830', ' 830'), ('831', ' 831'), ('832', ' 832'), ('833', ' 833'), ('834', ' 834'), ('835', ' 835'), ('836', ' 836'), ('837', ' 837'), ('838', ' 838'), ('839', ' 839'), ('840', ' 840'), ('841', ' 841'), ('842', ' 842'), ('843', ' 843'), ('844', ' 844'), ('845', ' 845'), ('846', ' 846'), ('847', ' 847'), ('848', ' 848'), ('849', ' 849'), ('850', ' 850'), ('851', ' 851'), ('852', ' 852'), ('853', ' 853'), ('854', ' 854'), ('855', ' 855'), ('856', ' 856'), ('857', ' 857'), ('858', ' 858'), ('859', ' 859'), ('860', ' 860'), ('861', ' 861'), ('862', ' 862'), ('863', ' 863'), ('864', ' 864'), ('865', ' 865'), ('866', ' 866'), ('867', ' 867'), ('868', ' 868'), ('869', ' 869')], default=None, max_length=100, null=True),
        ),
    ]
