# Render MicroAPI 
API I created for myself to do a quick check on my projects. Maybe will add more. 

---

## Stack
- Python 3.12
- FastAPI

---
## Endpoints
| url                               | Verb |
|-----------------------------------| -----|
| /api/services                     | GET  |
| /api/services/{service_id}/restart| POST |
| /api/services/{service_id}/resume | POST |
| /api/services/{service_id}/suspend| POST |
| /api/services/list_postgres       | GET  |

---

## Runing
Just set an .env file on root with the next shape:
```text
RENDER_API_KEY =""
RENDER_LIMIT =""
RENDER_API_URL =""
```
---

