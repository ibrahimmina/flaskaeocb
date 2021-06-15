import click
from app import app, db
from app.models import User, Post, Role, UserRoles, Theme, Country, UserCountries

@app.cli.command('resetcounties')
def resetcounties_command():
    print ("resetcounties")
    #for all records
    db.session.query(Role).delete()
    db.session.commit()
    db.session.add(Role(name='Admin'))
    db.session.commit()
    db.session.query(Country).delete()
    db.session.commit()
    db.session.add(Country(name='Andorra', code='AD', status=0))
    db.session.add(Country(name='United Arab Emirates', code='AE', status=0))
    db.session.add(Country(name='Afghanistan', code='AF', status=0))
    db.session.add(Country(name='Antigua and Barbuda', code='AG', status=0))
    db.session.add(Country(name='Anguilla', code='AI', status=0))
    db.session.add(Country(name='Albania', code='AL', status=0))
    db.session.add(Country(name='Armenia', code='AM', status=0))
    db.session.add(Country(name='Netherlands Antilles', code='AN', status=0))
    db.session.add(Country(name='Angola', code='AO', status=0))
    db.session.add(Country(name='Antarctica', code='AQ', status=0))
    db.session.add(Country(name='Argentina', code='AR', status=0))
    db.session.add(Country(name='American Samoa', code='AS', status=0))
    db.session.add(Country(name='Austria', code='AT', status=0))
    db.session.add(Country(name='Australia', code='AU', status=0))
    db.session.add(Country(name='Aruba', code='AW', status=0))
    db.session.add(Country(name='Åland Islands', code='AX', status=0))
    db.session.add(Country(name='Azerbaijan', code='AZ', status=0))
    db.session.add(Country(name='Bosnia and Herzegovina', code='BA', status=0))
    db.session.add(Country(name='Barbados', code='BB', status=0))
    db.session.add(Country(name='Bangladesh', code='BD', status=0))
    db.session.add(Country(name='Belgium', code='BE', status=0))
    db.session.add(Country(name='Burkina Faso', code='BF', status=0))
    db.session.add(Country(name='Bulgaria', code='BG', status=0))
    db.session.add(Country(name='Bahrain', code='BH', status=0))
    db.session.add(Country(name='Burundi', code='BI', status=0))
    db.session.add(Country(name='Benin', code='BJ', status=0))
    db.session.add(Country(name='Saint Barthélemy', code='BL', status=0))
    db.session.add(Country(name='Bermuda', code='BM', status=0))
    db.session.add(Country(name='Brunei Darussalam', code='BN', status=0))
    db.session.add(Country(name='Bolivia', code='BO', status=0))
    db.session.add(Country(name='Bonaire Sint Eustatius and Saba', code='BQ', status=0))
    db.session.add(Country(name='Brazil', code='BR', status=0))
    db.session.add(Country(name='Bahamas', code='BS', status=0))
    db.session.add(Country(name='Bhutan', code='BT', status=0))
    db.session.add(Country(name='Bouvet Island', code='BV', status=0))
    db.session.add(Country(name='Botswana', code='BW', status=0))
    db.session.add(Country(name='Belarus', code='BY', status=0))
    db.session.add(Country(name='Belize', code='BZ', status=0))
    db.session.add(Country(name='Canada', code='CA', status=0))
    db.session.add(Country(name='Cocos (Keeling) Islands', code='CC', status=0))
    db.session.add(Country(name='Congo The Democratic Republic Of The', code='CD', status=0))
    db.session.add(Country(name='Central African Republic', code='CF', status=0))
    db.session.add(Country(name='Congo', code='CG', status=0))
    db.session.add(Country(name='Switzerland', code='CH', status=0))
    db.session.add(Country(name='Côte DIvoire', code='CI', status=0))
    db.session.add(Country(name='Cook Islands', code='CK', status=0))
    db.session.add(Country(name='Chile', code='CL', status=0))
    db.session.add(Country(name='Cameroon', code='CM', status=0))
    db.session.add(Country(name='China', code='CN', status=0))
    db.session.add(Country(name='Colombia', code='CO', status=0))
    db.session.add(Country(name='Costa Rica', code='CR', status=0))
    db.session.add(Country(name='Cuba', code='CU', status=0))
    db.session.add(Country(name='Cape Verde', code='CV', status=0))
    db.session.add(Country(name='Curaçao', code='CW', status=0))
    db.session.add(Country(name='Christmas Island', code='CX', status=0))
    db.session.add(Country(name='Cyprus', code='CY', status=0))
    db.session.add(Country(name='Czech Republic', code='CZ', status=0))
    db.session.add(Country(name='Germany', code='DE', status=0))
    db.session.add(Country(name='Djibouti', code='DJ', status=0))
    db.session.add(Country(name='Denmark', code='DK', status=0))
    db.session.add(Country(name='Dominica', code='DM', status=0))
    db.session.add(Country(name='Dominican Republic', code='DO', status=0))
    db.session.add(Country(name='Algeria', code='DZ', status=0))
    db.session.add(Country(name='Ecuador', code='EC', status=0))
    db.session.add(Country(name='Estonia', code='EE', status=0))
    db.session.add(Country(name='Egypt', code='EG', status=0))
    db.session.add(Country(name='Western Sahara', code='EH', status=0))
    db.session.add(Country(name='Eritrea', code='ER', status=0))
    db.session.add(Country(name='Spain', code='ES', status=0))
    db.session.add(Country(name='Ethiopia', code='ET', status=0))
    db.session.add(Country(name='Finland', code='FI', status=0))
    db.session.add(Country(name='Fiji', code='FJ', status=0))
    db.session.add(Country(name='Falkland Islands (Malvinas)', code='FK', status=0))
    db.session.add(Country(name='Micronesia Federated States Of', code='FM', status=0))
    db.session.add(Country(name='Faroe Islands', code='FO', status=0))
    db.session.add(Country(name='France', code='FR', status=0))
    db.session.add(Country(name='Gabon', code='GA', status=0))
    db.session.add(Country(name='United Kingdom', code='GB', status=0))
    db.session.add(Country(name='Grenada', code='GD', status=0))
    db.session.add(Country(name='Georgia', code='GE', status=0))
    db.session.add(Country(name='French Guiana', code='GF', status=0))
    db.session.add(Country(name='Guernsey', code='GG', status=0))
    db.session.add(Country(name='Ghana', code='GH', status=0))
    db.session.add(Country(name='Gibraltar', code='GI', status=0))
    db.session.add(Country(name='Greenland', code='GL', status=0))
    db.session.add(Country(name='Gambia', code='GM', status=0))
    db.session.add(Country(name='Guinea', code='GN', status=0))
    db.session.add(Country(name='Guadeloupe', code='GP', status=0))
    db.session.add(Country(name='Equatorial Guinea', code='GQ', status=0))
    db.session.add(Country(name='Greece', code='GR', status=0))
    db.session.add(Country(name='South Georgia and the South Sandwich Islands', code='GS', status=0))
    db.session.add(Country(name='Guatemala', code='GT', status=0))
    db.session.add(Country(name='Guam', code='GU', status=0))
    db.session.add(Country(name='Guinea-Bissau', code='GW', status=0))
    db.session.add(Country(name='Guyana', code='GY', status=0))
    db.session.add(Country(name='Hong Kong', code='HK', status=0))
    db.session.add(Country(name='Heard and McDonald Islands', code='HM', status=0))
    db.session.add(Country(name='Honduras', code='HN', status=0))
    db.session.add(Country(name='Croatia', code='HR', status=0))
    db.session.add(Country(name='Haiti', code='HT', status=0))
    db.session.add(Country(name='Hungary', code='HU', status=0))
    db.session.add(Country(name='Indonesia', code='ID', status=0))
    db.session.add(Country(name='Ireland', code='IE', status=0))
    db.session.add(Country(name='Israel', code='IL', status=0))
    db.session.add(Country(name='Isle of Man', code='IM', status=0))
    db.session.add(Country(name='India', code='IN', status=0))
    db.session.add(Country(name='British Indian Ocean Territory', code='IO', status=0))
    db.session.add(Country(name='Iraq', code='IQ', status=0))
    db.session.add(Country(name='Iran Islamic Republic Of', code='IR', status=0))
    db.session.add(Country(name='Iceland', code='IS', status=0))
    db.session.add(Country(name='Italy', code='IT', status=0))
    db.session.add(Country(name='Jersey', code='JE', status=0))
    db.session.add(Country(name='Jamaica', code='JM', status=0))
    db.session.add(Country(name='Jordan', code='JO', status=0))
    db.session.add(Country(name='Japan', code='JP', status=0))
    db.session.add(Country(name='Kenya', code='KE', status=0))
    db.session.add(Country(name='Kyrgyzstan', code='KG', status=0))
    db.session.add(Country(name='Cambodia', code='KH', status=0))
    db.session.add(Country(name='Kiribati', code='KI', status=0))
    db.session.add(Country(name='Comoros', code='KM', status=0))
    db.session.add(Country(name='Saint Kitts And Nevis', code='KN', status=0))
    db.session.add(Country(name='Korea Democratic Peoples Republic Of', code='KP', status=0))
    db.session.add(Country(name='Korea Republic of', code='KR', status=0))
    db.session.add(Country(name='Kuwait', code='KW', status=0))
    db.session.add(Country(name='Cayman Islands', code='KY', status=0))
    db.session.add(Country(name='Kazakhstan', code='KZ', status=0))
    db.session.add(Country(name='Lao Peoples Democratic Republic', code='LA', status=0))
    db.session.add(Country(name='Lebanon', code='LB', status=0))
    db.session.add(Country(name='Saint Lucia', code='LC', status=0))
    db.session.add(Country(name='Liechtenstein', code='LI', status=0))
    db.session.add(Country(name='Sri Lanka', code='LK', status=0))
    db.session.add(Country(name='Liberia', code='LR', status=0))
    db.session.add(Country(name='Lesotho', code='LS', status=0))
    db.session.add(Country(name='Lithuania', code='LT', status=0))
    db.session.add(Country(name='Luxembourg', code='LU', status=0))
    db.session.add(Country(name='Latvia', code='LV', status=0))
    db.session.add(Country(name='Libya', code='LY', status=0))
    db.session.add(Country(name='Morocco', code='MA', status=0))
    db.session.add(Country(name='Monaco', code='MC', status=0))
    db.session.add(Country(name='Moldova Republic of', code='MD', status=0))
    db.session.add(Country(name='Montenegro', code='ME', status=0))
    db.session.add(Country(name='Saint Martin', code='MF', status=0))
    db.session.add(Country(name='Madagascar', code='MG', status=0))
    db.session.add(Country(name='Marshall Islands', code='MH', status=0))
    db.session.add(Country(name='Macedonia the Former Yugoslav Republic Of', code='MK', status=0))
    db.session.add(Country(name='Mali', code='ML', status=0))
    db.session.add(Country(name='Myanmar', code='MM', status=0))
    db.session.add(Country(name='Mongolia', code='MN', status=0))
    db.session.add(Country(name='Macao', code='MO', status=0))
    db.session.add(Country(name='Northern Mariana Islands', code='MP', status=0))
    db.session.add(Country(name='Martinique', code='MQ', status=0))
    db.session.add(Country(name='Mauritania', code='MR', status=0))
    db.session.add(Country(name='Montserrat', code='MS', status=0))
    db.session.add(Country(name='Malta', code='MT', status=0))
    db.session.add(Country(name='Mauritius', code='MU', status=0))
    db.session.add(Country(name='Maldives', code='MV', status=0))
    db.session.add(Country(name='Malawi', code='MW', status=0))
    db.session.add(Country(name='Mexico', code='MX', status=0))
    db.session.add(Country(name='Malaysia', code='MY', status=0))
    db.session.add(Country(name='Mozambique', code='MZ', status=0))
    db.session.add(Country(name='Namibia', code='NA', status=0))
    db.session.add(Country(name='New Caledonia', code='NC', status=0))
    db.session.add(Country(name='Niger', code='NE', status=0))
    db.session.add(Country(name='Norfolk Island', code='NF', status=0))
    db.session.add(Country(name='Nigeria', code='NG', status=0))
    db.session.add(Country(name='Nicaragua', code='NI', status=0))
    db.session.add(Country(name='Netherlands', code='NL', status=0))
    db.session.add(Country(name='Norway', code='NO', status=0))
    db.session.add(Country(name='Nepal', code='NP', status=0))
    db.session.add(Country(name='Nauru', code='NR', status=0))
    db.session.add(Country(name='Niue', code='NU', status=0))
    db.session.add(Country(name='New Zealand', code='NY', status=0))
    db.session.add(Country(name='Oman', code='OM', status=0))
    db.session.add(Country(name='Panama', code='PA', status=0))
    db.session.add(Country(name='Peru', code='PE', status=0))
    db.session.add(Country(name='French Polynesia', code='PF', status=0))
    db.session.add(Country(name='Papua New Guinea', code='PG', status=0))
    db.session.add(Country(name='Philippines', code='PH', status=0))
    db.session.add(Country(name='Pakistan', code='PK', status=0))
    db.session.add(Country(name='Poland', code='PL', status=0))
    db.session.add(Country(name='Saint Pierre And Miquelon', code='PM', status=0))
    db.session.add(Country(name='Pitcairn', code='PN', status=0))
    db.session.add(Country(name='Puerto Rico', code='PR', status=0))
    db.session.add(Country(name='Palestine State of', code='PS', status=0))
    db.session.add(Country(name='Portugal', code='PT', status=0))
    db.session.add(Country(name='Palau', code='PW', status=0))
    db.session.add(Country(name='Paraguay', code='PY', status=0))
    db.session.add(Country(name='Qatar', code='QA', status=0))
    db.session.add(Country(name='Réunion', code='RE', status=0))
    db.session.add(Country(name='Romania', code='RO', status=0))
    db.session.add(Country(name='Serbia', code='RS', status=0))
    db.session.add(Country(name='Russian Federation', code='RU', status=0))
    db.session.add(Country(name='Rwanda', code='RW', status=0))
    db.session.add(Country(name='Saudi Arabia', code='SA', status=0))
    db.session.add(Country(name='Solomon Islands', code='SB', status=0))
    db.session.add(Country(name='Seychelles', code='SC', status=0))
    db.session.add(Country(name='Sudan', code='SD', status=0))
    db.session.add(Country(name='Sweden', code='SE', status=0))
    db.session.add(Country(name='Singapore', code='SG', status=0))
    db.session.add(Country(name='Saint Helena', code='SH', status=0))
    db.session.add(Country(name='Slovenia', code='SI', status=0))
    db.session.add(Country(name='Svalbard And Jan Mayen', code='SJ', status=0))
    db.session.add(Country(name='Slovakia', code='SK', status=0))
    db.session.add(Country(name='Sierra Leone', code='SL', status=0))
    db.session.add(Country(name='San Marino', code='SM', status=0))
    db.session.add(Country(name='Senegal', code='SN', status=0))
    db.session.add(Country(name='Somalia', code='SO', status=0))
    db.session.add(Country(name='Suriname', code='SR', status=0))
    db.session.add(Country(name='South Sudan', code='SS', status=0))
    db.session.add(Country(name='Sao Tome and Principe', code='ST', status=0))
    db.session.add(Country(name='El Salvador', code='SV', status=0))
    db.session.add(Country(name='Sint Maarten', code='SX', status=0))
    db.session.add(Country(name='Syrian Arab Republic', code='SY', status=0))
    db.session.add(Country(name='Swaziland', code='SZ', status=0))
    db.session.add(Country(name='Turks and Caicos Islands', code='TC', status=0))
    db.session.add(Country(name='Chad', code='TD', status=0))
    db.session.add(Country(name='French Southern Territories', code='TF', status=0))
    db.session.add(Country(name='Togo', code='TG', status=0))
    db.session.add(Country(name='Thailand', code='TH', status=0))
    db.session.add(Country(name='Tajikistan', code='TJ', status=0))
    db.session.add(Country(name='Tokelau', code='TK', status=0))
    db.session.add(Country(name='Timor-Leste', code='TL', status=0))
    db.session.add(Country(name='Turkmenistan', code='TM', status=0))
    db.session.add(Country(name='Tunisia', code='TN', status=0))
    db.session.add(Country(name='Tonga', code='TO', status=0))
    db.session.add(Country(name='Turkey', code='TR', status=0))
    db.session.add(Country(name='Trinidad and Tobago', code='TT', status=0))
    db.session.add(Country(name='Tuvalu', code='TV', status=0))
    db.session.add(Country(name='Taiwan Republic Of China', code='TW', status=0))
    db.session.add(Country(name='Tanzania United Republic of', code='TZ', status=0))
    db.session.add(Country(name='Ukraine', code='UA', status=0))
    db.session.add(Country(name='Uganda', code='UG', status=0))
    db.session.add(Country(name='United States Minor Outlying Islands', code='UM', status=0))
    db.session.add(Country(name='United States', code='US', status=0))
    db.session.add(Country(name='Uruguay', code='UY', status=0))
    db.session.add(Country(name='Uzbekistan', code='UZ', status=0))
    db.session.add(Country(name='Holy See (Vatican City State)', code='VA', status=0))
    db.session.add(Country(name='Saint Vincent And The Grenadines', code='VC', status=0))
    db.session.add(Country(name='Venezuela Bolivarian Republic of', code='VE', status=0))
    db.session.add(Country(name='Virgin Islands British', code='VG', status=0))
    db.session.add(Country(name='Virgin Islands U.S.', code='VI', status=0))
    db.session.add(Country(name='Vietnam', code='VN', status=0))
    db.session.add(Country(name='Vanuatu', code='VU', status=0))
    db.session.add(Country(name='Wallis and Futuna', code='WF', status=0))
    db.session.add(Country(name='Samoa', code='WS', status=0))
    db.session.add(Country(name='Yemen', code='YE', status=0))
    db.session.add(Country(name='Mayotte', code='YT', status=0))
    db.session.add(Country(name='South Africa', code='ZA', status=0))
    db.session.add(Country(name='Zambia', code='ZM', status=0))
    db.session.add(Country(name='Zimbabwe', code='ZW', status=0))

    db.session.commit()
    pass
