/**
 * IndexedDB Utility for storing, retrieving, and deleting images locally.
 * 
 * Functions:
 *   - initDB: Initializes or upgrades the IndexedDB database. Used internally by other functions.
 *   - addImage: Adds or updates an image object in the IndexedDB "images" store.
 *   - getAllImages: Retrieves all stored image objects from IndexedDB.
 *   - deleteImage: Deletes a specific image from IndexedDB by its id.
 *   - clearImages: Deletes all images from the IndexedDB "images" store.
 */

const DB_NAME = 'ImageSyncDB';
const DB_VERSION = 1;
const STORE_NAME = 'images';

/**
 * Initialize or upgrade the IndexedDB database.
 * Handles creation of the object store if it doesn't exist.
 * @returns {Promise<IDBDatabase>}
 */
function initDB() {
  return new Promise((resolve, reject) => {
    const request = window.indexedDB.open(DB_NAME, DB_VERSION);

    request.onerror = (e) => reject('IndexedDB error: ' + e.target.errorCode);

    request.onupgradeneeded = (e) => {
      const db = e.target.result;
      // Create the object store for images if it doesn't already exist
      if (!db.objectStoreNames.contains(STORE_NAME)) {
        db.createObjectStore(STORE_NAME, { keyPath: 'id' });
      }
    };

    request.onsuccess = (e) => resolve(e.target.result);
  });
}

/**
 * Add or update an image object in IndexedDB.
 * @param {Object} imageObj - The image object to store. Example: { id, name, data (Blob), cloudinaryId, ... }
 * @returns {Promise<boolean>} Resolves to true if success.
 */
export async function addImage(imageObj) {
  const db = await initDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_NAME, 'readwrite');
    const store = tx.objectStore(STORE_NAME);
    store.put(imageObj);
    tx.oncomplete = () => resolve(true);
    tx.onerror = (e) => reject('IndexedDB add error: ' + e.target.errorCode);
  });
}

/**
 * Retrieve all image objects from IndexedDB.
 * @returns {Promise<Array>} Resolves to an array of image objects.
 */
export async function getAllImages() {
  const db = await initDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_NAME, 'readonly');
    const store = tx.objectStore(STORE_NAME);
    const request = store.getAll();
    request.onsuccess = (e) => resolve(e.target.result);
    request.onerror = (e) => reject('IndexedDB getAll error: ' + e.target.errorCode);
  });
}

/**
 * Delete a specific image from IndexedDB based on its id.
 * @param {string|number} id - The id of the image to delete.
 * @returns {Promise<boolean>} Resolves to true if success.
 */
export async function deleteImage(id) {
  const db = await initDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_NAME, 'readwrite');
    const store = tx.objectStore(STORE_NAME);
    store.delete(id);
    tx.oncomplete = () => resolve(true);
    tx.onerror = (e) => reject('IndexedDB delete error: ' + e.target.errorCode);
  });
}

/**
 * Delete all images from the IndexedDB store.
 * @returns {Promise<boolean>} Resolves to true if success.
 */
export async function clearImages() {
  const db = await initDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_NAME, 'readwrite');
    const store = tx.objectStore(STORE_NAME);
    store.clear();
    tx.oncomplete = () => resolve(true);
    tx.onerror = (e) => reject('IndexedDB clear error: ' + e.target.errorCode);
  });
}