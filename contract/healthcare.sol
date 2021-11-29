pragma solidity >=0.7.0 <0.9.0;

contract healtCare {
    uint public pidCount;
    uint public doctorCount;
    
    struct Patient{
        string username;
        string name;
        string email;
        uint age;
        string addres;
        uint mobile;
        string password;
    }
    
    struct Doctor{
        string username;
        string name;
        string email;
        uint age;
        string addres;
        uint mobile;
        uint registrationNo;
        string qualification;
        string password;
    }
    
    event newPatientCreated(string username,string _name,string email,uint age,string addres,uint mobile,string password);
    event newDoctorCreated(string username,string name,string email,uint age,string addres,uint mobile,uint registrationNo,string qualification,string password);
    
    mapping(address=> Patient) public patientList;

    mapping(address=>Doctor) public doctorList;
    
    
    
    function setPatientData(string memory _username,string memory _name,string memory _email,uint _age, string memory _addres,uint _mobile, string memory _password) public {
        address pid = address(bytes20(keccak256(abi.encodePacked(msg.sender,block.timestamp))));
        patientList[pid]=Patient(_username,_name,_email,_age,_addres,_mobile,_password);
        pidCount++;
        emit newPatientCreated(_username,_name,_email,_age,_addres,_mobile,_password);
    }
    
    function setDoctorData(string memory _username,string memory _name,string memory _email,uint _age,string memory _addres,uint _mobile,uint _registraionNo,string memory _qualification,string memory _password)public{
        address doctorid = address(bytes20(keccak256(abi.encodePacked(msg.sender,block.timestamp))));
        doctorList[doctorid] = Doctor(_username,_name,_email,_age,_addres,_mobile,_registraionNo,_qualification,_password);
        doctorCount++;
        emit newDoctorCreated(_username,_name,_email,_age,_addres,_mobile,_registraionNo,_qualification,_password);
    }
    
}
