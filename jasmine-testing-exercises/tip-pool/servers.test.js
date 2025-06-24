describe("Servers test (with setup and tear-down)", function() {
  beforeEach(function () {
    // initialization logic
    serverNameInput.value = 'Alice';
  });

  it('should add a new server to allServers on submitServerInfo()', function () {
    submitServerInfo();

    expect(Object.keys(allServers).length).toEqual(1);
    expect(allServers['server' + serverId].serverName).toEqual('Alice');
  });

  afterEach(function() {
    // teardown logic
    // Remove all rows from server table
    serverTbody.innerHTML = '';
    // Reset allServers and serverId
    allServers = {};
    serverId = 0;
    serverNameInput.value = '';
  });

  it('should not add a server with empty name', function() {
    serverNameInput.value = '';
    submitServerInfo();
    expect(Object.keys(allServers).length).toEqual(0);
    expect(serverTbody.children.length).toEqual(0);
  });

  it('should update the server table with correct data', function() {
    serverNameInput.value = 'Bob';
    submitServerInfo();
    // Should add one row
    expect(serverTbody.children.length).toEqual(1);
    const row = serverTbody.children[0];
    expect(row.querySelector('td').innerText).toEqual('Bob');
  });

  it('should call appendTd for each server row', function() {
    spyOn(window, 'appendTd').and.callThrough();
    serverNameInput.value = 'Carol';
    submitServerInfo();
    expect(appendTd).toHaveBeenCalled();
    // Two tds per row: name and tip average
    expect(appendTd.calls.count()).toBe(2);
  });

  it('should remove a server row when delete button is clicked', function() {
    serverNameInput.value = 'Dave';
    submitServerInfo();
    expect(serverTbody.children.length).toBe(1);
    const row = serverTbody.children[0];
    const deleteBtn = row.querySelector('td.deleteBtn');
    expect(deleteBtn).not.toBeNull();
    deleteBtn.click();
    expect(serverTbody.children.length).toBe(0);
  });
});
