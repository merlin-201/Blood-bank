from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
import pymysql
from datetime import date
 
app = Flask(__name__)
app.secret_key = "Ninad-Patil"
  
mysql = MySQL()
   
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'blood_bank'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

tab = "home"
donor_tab = "home"

def updateStock(volume, bld_grp):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute('SELECT * FROM stock')
    stocks = cur.fetchall()

    for stock in stocks:
        if stock['blood_group'] == bld_grp:
            new_volume = stock['volume'] + volume
            break

    query ='''
    UPDATE stock
    SET volume = {}
    WHERE blood_group = "{}"
    '''.format(new_volume, bld_grp)

    cur.execute(query)
    conn.commit()

def giveLatestDonor():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute('SELECT * FROM donor')
    donors = cur.fetchall()

    all_dids = []
    for donor in donors:
        all_dids.append( donor['donor_id'] )
    
    return int(max(all_dids))

def getDashboardInfo():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute('SELECT * FROM donor')
    donors = cur.fetchall()

    cur.execute('SELECT * FROM donation')
    donations = cur.fetchall()

    cur.execute('SELECT * FROM request')
    requests = cur.fetchall()

    dashboard_info = {'total_donors':0,'total_donated_today':0,'todays_requests':0,'todays_approved_requests':0}

    dashboard_info['total_donors'] = len(donors)

    today = str(date.today())
    for donation in donations:
        if str(donation['date_of_donation']) == today:
            dashboard_info['total_donated_today'] += 1
    
    for request in requests:
        # print("comparing {} and {}\n\n".format(request['date_of_request'],today))
        if str(request['date_of_request']) == today:
            dashboard_info['todays_requests'] += 1

        if str(request['date_of_approval']) == today and request['status'] == "Approved":
            dashboard_info['todays_approved_requests'] += 1

    
    # print(today)
    # print(dashboard_info)

    return dashboard_info






#----------------- Landing Page Routes -------------------

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/donorRegistration', methods=['GET','POST'])
def donorRegistration():
    return render_template('regis_form.html')

@app.route('/register_donor', methods=['POST'])
def register_donor():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        name = request.form['fullname']
        email = request.form['email']
        contact = request.form['contact']
        password = request.form['password']
        blood_group = request.form['bloodgroup']
        gender = request.form['gender']
        weight = request.form['weight']
        dob = request.form['date_of_birth']
        state = request.form['state']
        district = request.form['district']
        city = request.form['city']
        address = request.form['address']
        lastdod = request.form['last_date_of_donation']

        query = '''INSERT INTO donor (donor_id, name, email, blood_group, gender, date_of_birth, weight, contact_number, state, district, city, address, last_date_of_donation)
         VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        
        cur.execute(query, (name, email, blood_group, gender, dob, weight, contact, state, district, city, address, lastdod))
        
        conn.commit()


        did = giveLatestDonor()

        login_query = '''INSERT INTO login (email, password, donor_id) VALUES ('{}', '{}', '{}')
        '''.format(email, password, did)

        cur.execute(login_query)

        conn.commit()


    return redirect('/donor/'+str(did))

@app.route('/search_donor', methods=['GET','POST'])
def search_donor():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    donors = []
    bld_grp = ""
    city = ""
    if request.method == 'POST':
        bld_grp = request.form['bloodgroup']
        city = request.form['city']

        query = " SELECT name, blood_group, contact_number FROM donor WHERE blood_group = '{}' and city = '{}' ".format(bld_grp, city)

        cur.execute( query )

        donors = cur.fetchall()


    return render_template('search_donor.html', donors=donors, city=city,bld_grp=bld_grp)





# -------------------- DONOR ROUTES -----------------------------

@app.route('/donor/<int:did>', methods=['GET','POST'])
def donor(did):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute('SELECT * FROM donor')
    donors = cur.fetchall()

    cur.execute('SELECT * FROM donation WHERE donor_id = {}'.format(did))
    mydonations = cur.fetchall()

    total_donations = len(mydonations)
    total_blood_donated = 0

    for donation in mydonations:
        total_blood_donated += donation['volume']

    donor_info = 0

    for donor in donors:
        if donor['donor_id'] == did:
            donor_info = donor
            break
    if donor_info != 0:
        return render_template('donor.html',tab = donor_tab, donor = donor_info, total_donations=total_donations, total_blood_donated = total_blood_donated  )
    else:
        return render_template('error.html')

@app.route('/edit_donor_info', methods=['POST'])
def edit_donor_info():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        did = int(request.form['donor_id'])
        name = request.form['fullname']
        email = request.form['email']
        contact = request.form['contact']
        blood_group = request.form['bloodgroup']
        gender = request.form['gender']
        state = request.form['state']
        district = request.form['district']
        city = request.form['city']
        address = request.form['address']

        query = '''
        UPDATE donor
        SET name = "{}", email = "{}", blood_group = "{}", gender = "{}", contact_number= "{}", state= "{}", district= "{}", city= "{}", address= "{}"
        WHERE donor_id = {}
        '''.format(name, email, blood_group, gender, contact, state, district, city, address, did)

        cur.execute(query)
        conn.commit()
    
    global donor_tab
    donor_tab = "editdetails"

    return redirect('/donor/'+str(did))






# -------------------- HOSPITAL ROUTES -----------------------------

@app.route('/hospital/<int:hid>', methods=['GET','POST'])
def hospital(hid):
    conn=mysql.connect()
    cur=conn.cursor(pymysql.cursors.DictCursor)

    query="SELECT * FROM `request` WHERE hospital_id={}".format(hid)
    cur.execute(query)
    myrequests = cur.fetchall()

    query = "SELECT name FROM hospital WHERE hospital_id={}".format(hid)
    cur.execute(query)
    hosp_name = cur.fetchall()[0]['name']
    
    return render_template('hospital.html',requests=myrequests, hid=hid, hosp_name= hosp_name)

@app.route('/hosp_make_request/<int:hid>', methods=['POST'])
def hosp_make_request(hid):
    conn=mysql.connect()
    cur=conn.cursor(pymysql.cursors.DictCursor)

    if request.method == 'POST':
        patient_name = request.form['patient_name']
        physician_name = request.form['physician_name']
        bld_grp = request.form['bloodgroup']
        volume = request.form['volume']
        date_of_req = request.form['date_of_request']

    query='''
    INSERT INTO `request` (`request_id`, `hospital_id`, `patient_name`, `physician_name`, `blood_group`, `volume_needed`, `status`, `date_of_request`, `date_of_approval`)
    VALUES (NULL, '{}', '{}', '{}', '{}', '{}', 'Pending', '{}', NULL);
    '''.format(hid, patient_name, physician_name, bld_grp, volume, date_of_req)

    cur.execute(query)
    conn.commit()

    return redirect('/hospital/'+str(hid))





    



# ----------------------  ADMIN ROUTES  --------------------------


@app.route('/admin')
def Admin():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute('SELECT * FROM donor')
    donors = cur.fetchall()

    cur.execute('SELECT * FROM donation')
    donations = cur.fetchall()

    for donation in donations:
        did = donation['donor_id']
        donation['donor_name'] = "UNKNOWN"
        donation['blood_group'] = "UNKNOWN"
        for donor in donors:
            if donor['donor_id'] == did:
                donation['donor_name'] = donor['name']
                donation['blood_group'] = donor['blood_group']
                break

    cur.execute('SELECT * FROM stock')
    stocks = cur.fetchall()

    stock_info = {}
    for stock in stocks:
        stock_info[ stock['blood_group'] ] = stock['volume']

    cur.execute('SELECT * FROM request')
    requests = cur.fetchall()

    dashboard = getDashboardInfo()


    cur.close()
    return render_template('admin.html',tab=tab, donors=donors, donations = donations, stock_info=stock_info, requests=requests, dashboard = dashboard)





# === DONORS TAB ===

@app.route('/add_donor', methods=['POST'])
def add_donor():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        name = request.form['fullname']
        email = request.form['email']
        contact = request.form['contact']
        blood_group = request.form['bloodgroup']
        gender = request.form['gender']
        weight = request.form['weight']
        dob = request.form['date_of_birth']
        state = request.form['state']
        district = request.form['district']
        city = request.form['city']
        address = request.form['address']
        lastdod = request.form['last_date_of_donation']
        query = '''INSERT INTO donor (donor_id, name, email, blood_group, gender, date_of_birth, weight, contact_number, state, district, city, address, last_date_of_donation)
         VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        cur.execute(query, (name, email, blood_group, gender, dob, weight, contact, state, district, city, address, lastdod))
        conn.commit()
    global tab
    tab = "donors"

    return redirect(url_for('Admin'))

@app.route('/edit_donor', methods=['POST'])
def edit_donor():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        did = int(request.form['donor_id'])
        print('\n\n\n',did)
        name = request.form['fullname']
        email = request.form['email']
        contact = request.form['contact']
        blood_group = request.form['bloodgroup']
        gender = request.form['gender']
        state = request.form['state']
        district = request.form['district']
        city = request.form['city']
        address = request.form['address']
        lastdod = request.form['last_date_of_donation']

        query = '''
        UPDATE donor
        SET name = "{}", email = "{}", blood_group = "{}", gender = "{}", contact_number= "{}", state= "{}", district= "{}", city= "{}", address= "{}", last_date_of_donation= "{}"
        WHERE donor_id = {}
        '''.format(name, email, blood_group, gender, contact, state, district, city, address, lastdod, did)

        cur.execute(query)
        conn.commit()

    global tab
    tab = "donors"

    return redirect(url_for('Admin'))

@app.route('/delete_donor', methods=['POST'])
def delete_donor():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        did = int(request.form['donor_id'])

        query = '''
        DELETE FROM donor
        WHERE donor_id = {}
        '''.format(did)

        cur.execute(query)
        conn.commit()

    global tab
    tab = "donors"
    return redirect(url_for('Admin'))







# === DONATIONS TAB ===

@app.route('/add_donation', methods=['POST'])
def add_donation():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        did = int(request.form['donor_id'])
        volume = int(request.form['volume'])
        dod = request.form['date_of_donation']

        query =  "INSERT INTO donation (donation_id, donor_id, volume, date_of_donation) VALUES (NULL, %s, %s, %s)"

        cur.execute('SELECT * FROM donor')
        donors = cur.fetchall()

        for donor in donors:
                if donor['donor_id'] == did:
                    bld_grp = donor['blood_group']
                    break

        updateStock(volume, bld_grp)

        cur.execute(query, (did, volume, dod))

        conn.commit()

    global tab
    tab = "donations"

    return redirect(url_for('Admin'))


@app.route('/delete_donation', methods=['POST'])
def delete_donation():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        don_id = int(request.form['donation_id'])

        query = '''
        DELETE FROM donation
        WHERE donation_id = {}
        '''.format(don_id)

        cur.execute(query)
        conn.commit()

    global tab
    tab = "donations"

    return redirect(url_for('Admin'))







# === REQUESTS TAB ===

@app.route('/add_request', methods=['POST'])
def add_request():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        physician_name = request.form['physician_name']
        hosp_id = request.form['hospital_id']
        bld_grp = request.form['bloodgroup']
        volume_needed = request.form['volume_needed']
        date_of_request = request.form['date_of_request']

        query = '''
        INSERT INTO request (request_id, hospital_id, patient_name, physician_name, blood_group, volume_needed, status, date_of_request, date_of_approval) 
        VALUES (NULL, %s, %s, %s, %s, %s, 'Pending', %s, NULL)
        '''
        cur.execute(query, (hosp_id, patient_name, physician_name, bld_grp, volume_needed, date_of_request))
        conn.commit()

    global tab
    tab = "requests"

    return redirect(url_for('Admin'))

@app.route('/delete_request', methods=['POST'])
def delete_request():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        request_id = int(request.form['request_id'])

        query = '''
        DELETE FROM request
        WHERE request_id = {}
        '''.format(request_id)

        cur.execute(query)
        conn.commit()

    global tab
    tab = "requests"

    return redirect(url_for('Admin'))

@app.route('/change_request_status', methods=['POST'])
def change_request_status():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST':
        req_id = int(request.form['request_id'])

        query = '''
        UPDATE request
        SET status = "Approved"
        WHERE request_id = {}
        '''.format(req_id)

        cur.execute('SELECT * FROM request')
        requests = cur.fetchall()

        for req in requests:
            if req['request_id'] == req_id:
                bld_grp = req['blood_group']
                vol_needed = req['volume_needed']
                editquery = "UPDATE `request` SET `date_of_approval` = '{}' WHERE `request`.`request_id` = {};".format(str(date.today()), req_id)
                print(editquery)
                cur.execute(editquery)
                conn.commit()
                break

        updateStock( -vol_needed, bld_grp)

        cur.execute(query)
        conn.commit()

    global tab
    tab = "requests"

    return redirect(url_for('Admin'))




if __name__ == "__main__":
    app.run(port=3000, debug=True)