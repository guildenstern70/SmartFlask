//
//  SmartFlask Project
//
//  Copyright (c) 2023 Alessio Saltarin
//  This software is distributed under ISC License.
//  See LICENSE.
//

function deleteEntry(id) {
    document.getElementById('modal_student_id').innerText = id;
    const deleteModal = new bootstrap.Modal(document.getElementById('deletemodal'));
    document.getElementById('delete_confirm').href= '/delete?student_id=' + id;
    deleteModal.show();
}